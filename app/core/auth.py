from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from jose import JWTError, jwt
SECRET_KEY = "my_super_secret_key"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"

def create_access_token(user_id, company_id, role):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload ={
    "sub":  str(user_id),
    "company_id": company_id,
    "role": role,
    "iat": datetime.now(timezone.utc),
        "exp": expire,
}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token



def decode_access_token(token: str):
    print(f"Current TOkeN: {token}")
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError as e:
        print(type(e).__name__)
        print(str(e))
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )