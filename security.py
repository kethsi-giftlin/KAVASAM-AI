import base64, hashlib, hmac, os, time
import jwt

JWT_SECRET = os.getenv("KAVASAM_JWT_SECRET", "change-this-local-secret-before-public-deployment")
JWT_ALG = "HS256"


def hash_password(password: str) -> str:
    salt=os.urandom(16)
    digest=hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210000)
    return base64.b64encode(salt).decode()+":"+base64.b64encode(digest).decode()

def verify_password(password: str, stored: str) -> bool:
    try:
        s,d=stored.split(":",1)
        salt=base64.b64decode(s); expected=base64.b64decode(d)
        actual=hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210000)
        return hmac.compare_digest(actual, expected)
    except Exception:
        return False

def make_token(user_id: int, email: str) -> str:
    return jwt.encode({"sub":str(user_id),"email":email,"exp":int(time.time())+60*60*8}, JWT_SECRET, algorithm=JWT_ALG)

def decode_token(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
