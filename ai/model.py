from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TEXTS=[
"urgent verify your account immediately click here", "your bank account will be blocked send otp now",
"claim your reward by clicking the link", "confirm your password immediately", "parcel delivery failed pay fee",
"send me the verification code right now", "your account has a security problem login now",
"meeting moved to 3 pm see you there", "please review the project document", "class starts at 10 am tomorrow",
"thank you for submitting the assignment", "team meeting is scheduled for monday", "your order was delivered",
"please find the report attached", "let us discuss the project tomorrow"
]
LABELS=["phishing"]*7+["normal"]*8
V=TfidfVectorizer(ngram_range=(1,2),lowercase=True)
X=V.fit_transform(TEXTS)
M=LogisticRegression(max_iter=1000).fit(X,LABELS)

def classify(text:str):
    p=M.predict_proba(V.transform([text]))[0]; i=p.argmax()
    return {"label":M.classes_[i],"confidence":round(float(p[i]),3)}
