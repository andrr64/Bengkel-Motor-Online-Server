from datetime import datetime, timedelta
from app.core.config import settings
from jose import jwt, JWTError, ExpiredSignatureError

def generate_email_token(email: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=2)
    payload = {
        "sub": email,
        "exp": expire
    }
    token = jwt.encode(payload, settings.SECRET_KEY_FOR_EMAIL, algorithm=settings.JWT_ALGORITHM)
    return token

def verify_email_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY_FOR_EMAIL, algorithms=[settings.JWT_ALGORITHM])
        email = payload.get("sub")
        return email
    except ExpiredSignatureError:
        # Token kadaluarsa
        return None
    except JWTError:
        # Token tidak valid
        return None