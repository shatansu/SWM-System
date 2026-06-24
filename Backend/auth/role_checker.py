from fastapi import HTTPException, Depends

from auth.dependencies import get_current_user


def require_role(required_role: str):

    def role_dependency(
        current_user=Depends(get_current_user)
    ):

        if current_user["role"] != required_role:

            raise HTTPException(
                status_code=403,
                detail="Access Denied"
            )

        return current_user

    return role_dependency