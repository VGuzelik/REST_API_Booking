from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.user.crud import UserCRUD
from app.user.dependencies import get_current_user
from app.user.models import User
from app.user.schemas import SUserAuth
from app.user.auth import (get_password_hash, authenticate_user,
                           create_access_token)

from app.exceptions import CredentialsException, UserAlreadyExistsException

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register')
async def register_user(user_data: SUserAuth):
    user_exists = await UserCRUD.get_obj_or_none(email=user_data.email)
    if user_exists:
        raise UserAlreadyExistsException
    has_pass = get_password_hash(user_data.password)
    await UserCRUD.create_obj(email=user_data.email, hashed_password=has_pass)
    return status.HTTP_201_CREATED


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth) -> dict:
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise CredentialsException
    access_token = create_access_token({'sub': user.id})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')


@router.get('/me')
async def get_current_user(user: User = Depends(get_current_user)):
    return user

