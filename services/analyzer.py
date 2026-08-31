import re
from urllib.parse import urlparse
from app.ai.model import classify

URGENCY=["urgent","immediately","right now","today","act now","final warning","within 24 hours","account will be blocked"]
CREDS=["password","otp","one time password","verification code","login","username","pin","credential"]
FINANCE=["bank","credit card","debit card","payment","refund","gift card","wire transfer","upi","money"]
SOCIAL=["manager","boss","ceo","secret","confidential","don't tell anyone","meeting","send the code"]
SHORTENERS=["bit.ly","tinyurl.com","t.co","is.gd"]

def hits(text, words): return [w for w in words if w in text.lower()]
def level(s):
    return "SAFE / LOW RISK" if s<=20 else "LOW CONCERN" if s<=40 else "MODERATE RISK" if s<=60 else "HIGH RISK" if s<=80 else "CRITICAL RISK"

def analyze_url(url):
    raw=url.strip(); candidate=raw if re.match(r"^https?://",raw,re.I) else "https://"+raw
    p=urlparse(candidate); host=p.hostname or ""; low=candidate.lower(); score=0; inds=[]
    if p.scheme!="https": score+=15; inds.append("No HTTPS")
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$",host): score+=30; inds.append("IP-address based host")
    if len(candidate)>100: score+=15; inds.append("Unusually long URL")
    if "@" in candidate: score+=20; inds.append("Contains @ character")
    if host.count(".")>=3: score+=10; inds.append("Many subdomain levels")
    if any(x in host for x in SHORTENERS): score+=15; inds.append("URL shortener")
    if any(w in low for w in ["login","verify","secure","update","account","payment"]) and ("-" in host or host.count(".")>=2): score+=10; inds.append("Potential impersonation / login lure")
    score=min(score,100)
    return {"url":raw,"risk_score":score,"risk_level":level(score),"indicators":inds or ["No obvious URL-structure warning signs"],"explanation":"This prototype checks URL structure. HTTPS is useful but does not prove a website is legitimate.","recommendations":["Verify the domain carefully.","Avoid entering credentials on unexpected pages.","Open important services from a trusted bookmark or official app."],"disclaimer":"Prototype URL assessment; it does not certify a website as safe."}

def analyze_text(text):
    score=0; inds=[]; factors=[]
    groups=[(URGENCY,25,"Urgency / pressure","Urgent or threatening language"),(CREDS,20,"Sensitive information request","Credential / OTP indicators"),(FINANCE,15,"Financial request","Financial or payment indicators"),(SOCIAL,15,"Social engineering pattern","Social engineering indicators")]
    for words,label,factor in [(a,b,c) for a,b,c in groups]:
        if hits(text,words): score+=label; inds.append(factor); factors.append(f"+{label} {factor}")
    ml=classify(text)
    if ml["label"]=="phishing": score+=20; inds.append("ML classifier found phishing-like language"); factors.append("+20 ML phishing signal")
    urls=re.findall(r"https?://\S+|www\.\S+",text)
    for u in urls:
        ur=analyze_url(u)
        if ur["risk_score"]>=60: score+=15; inds.append("Suspicious URL structure"); factors.append("+15 Suspicious URL signal"); break
    score=min(score,100)
    threat="PHISHING / SOCIAL ENGINEERING" if score>=61 else "SUSPICIOUS CONTENT" if score>=41 else "NO STRONG THREAT SIGNAL"
    if score>=61:
        explanation="This content combines indicators commonly seen in phishing or social engineering. Pressure plus requests for sensitive information are strong warning signs."
        rec=["Do not click suspicious links.","Never share passwords, OTPs, PINs, or verification codes.","Open the official service directly instead of using the message link.","Verify unexpected requests through a trusted channel."]
    elif score>=41:
        explanation="Several warning signs are present. Pause and verify the request independently before responding."
        rec=["Pause before responding.","Verify the sender independently.","Avoid sharing sensitive information."]
    else:
        explanation="No strong phishing signals were detected by this prototype. That is not a guarantee of safety."
        rec=["Continue checking unexpected requests carefully.","Never share OTPs or passwords with others."]
    return {"risk_score":score,"risk_level":level(score),"threat_type":threat,"indicators":inds or ["No major rule-based warning signs"],"risk_factors":factors or ["No major risk factors detected"],"ml_signal":ml,"explanation":explanation,"recommendations":rec,"disclaimer":"Prototype assessment only; risk scores are not absolute truth."}
