from fastapi import Depends, HTTPException

from auth.jwt_handler import verify_access_token

from fastapi import Header



def get_current_user(
    authorization: str = Header(...)
):

    try:
        token = authorization.split(" ")[1]

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid Authorization Header"
        )

    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return payload