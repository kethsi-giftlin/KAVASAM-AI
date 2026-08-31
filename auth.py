from fastapi import Header, HTTPException
from app.security import decode_token

def current_user(authorization: str = Header(default="")) -> dict:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Login required")
    try:
        return decode_token(authorization.split(" ",1)[1])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
