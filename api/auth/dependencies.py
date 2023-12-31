from fastapi import Header, status
from fastapi.exceptions import HTTPException

from api.auth.authorization import get_data_form_token, get_current_user
from core.database import SessionLocal


def jwt_required(authorization=Header(None)):
    """Use this dependency to check token and get current user
    """
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is missing.")
    data = get_data_form_token(authorization)
    return get_current_user(data)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
