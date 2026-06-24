from fastapi import APIRouter, HTTPException

from models.user_model import UserRegister

from services.auth_service import register_user

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