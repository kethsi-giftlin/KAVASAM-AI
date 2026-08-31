def answer(message):
    t=message.lower()
    if "phishing" in t: a="Phishing is a social-engineering attack in which someone pretends to be a trusted person or organization to steal information or money. Common signs include urgency, fake links, impersonation, and requests for passwords or OTPs."
    elif "otp" in t: a="Never share an OTP with someone who contacts you unexpectedly. An OTP is meant to verify an action you initiated. If someone pressures you to read it out, stop and verify the request."
    elif "password" in t: a="Use a long, unique password for every important account. A password manager can help with unique passwords, and MFA adds another layer of protection."
    elif "clicked" in t or "suspicious link" in t: a="Stop interacting with the page. Do not enter credentials or payment details. If you entered a password, change it from the official website and enable MFA."
    elif "mfa" in t or "multi-factor" in t: a="MFA adds another verification step after your password. It can reduce the impact of a stolen password."
    elif "scam" in t: a="Common scam signals include unexpected contact, urgency, secrecy, unusual payment requests, and requests for verification codes. Pause and independently verify."
    else: a="I can help with phishing, suspicious links, passwords, OTPs, MFA, scams, social engineering, and safe browsing. Ask a cybersecurity question in simple language."
    return {"answer":a}
