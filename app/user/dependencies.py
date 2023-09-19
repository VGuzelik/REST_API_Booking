from datetime import datetime

import jwt
from fastapi import Depends, Request

from app.config import jwt_settings as jwt_s
from app.exceptions import CredentialsException
from app.user.crud import UserCRUD

# from fastapi.security import OAuth2PasswordBearer


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


def get_token(request: Request) -> str:
    token = request.cookies.get('booking_access_token')
    if not token:
        raise CredentialsException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload: dict = jwt.decode(
            token,
            jwt_s.SECRET_KEY,
            algorithms=[jwt_s.ALGORITHM],
        )
    except jwt.InvalidTokenError:
        raise CredentialsException

    expire: str = payload.get('exp')
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise CredentialsException

    user_id: str = payload.get('sub')
    if not user_id:
        raise CredentialsException

    user = await UserCRUD.get_obj_by_id(int(user_id))

    if not user:
        raise CredentialsException

    return user
