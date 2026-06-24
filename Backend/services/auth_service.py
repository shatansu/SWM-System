from db.mongodb_connection import users_collection

from auth.password import hash_password
from auth.password import verify_password
from auth.jwt_handler import create_access_token


def register_user(user):

    existing_user = users_collection.find_one(
        {
            "email": user.email
        }
    )

    if existing_user:

        return None

    user_data = {

        "name": user.name,

        "email": user.email,

        "password": hash_password(user.password),

        "role": user.role
    }

    result = users_collection.insert_one(
        user_data
    )

    return str(result.inserted_id)


def login_user(user):

    existing_user = users_collection.find_one(
        {
            "email": user.email
        }
    )

    if not existing_user:
        return None

    password_valid = verify_password(
        user.password,
        existing_user["password"]
    )

    if not password_valid:
        return None

    token = create_access_token(
        {
            "user_id": str(existing_user["_id"]),
            "role": existing_user["role"]
        }
    )

    return token