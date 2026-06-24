from fastapi import APIRouter, HTTPException,Header
from models.user_model import (
    UserRegister,
    UserLogin
)

from services.auth_service import (
    register_user,
    login_user
)


from fastapi import Depends

from auth.dependencies import get_current_user




router = APIRouter()


@router.post("/auth/register")
def register(user: UserRegister):

    user_id = register_user(user)

    if user_id is None:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return {

        "message": "User registered successfully",

        "user_id": user_id
    }



@router.post("/auth/login")
def login(user: UserLogin):

    token = login_user(user)

    if token is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Email or Password"
        )

    return {
        "access_token": token,
        "token_type": "Bearer"
    }



@router.get("/auth/me")
def me(
    authorization: str = Header(...)
):
    return {
        "header": authorization
    }