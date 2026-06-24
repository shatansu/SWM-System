from db.mongodb_connection import users_collection

from auth.password import hash_password


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