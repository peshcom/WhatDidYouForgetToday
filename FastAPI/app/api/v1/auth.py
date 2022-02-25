from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from ...database import get_db
from ...crud.users import get_user_by_login
from ...schemas.user import UserScheme

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

"""
https://indominusbyte.github.io/fastapi-jwt-auth/usage/refresh/

login:
curl -X POST http://localhost/v1/auth/login -H "Content-Type: application/json" -d '{"login":"admin","password":"password"}'
"""


@router.post('/login')
def login(
        user: UserScheme,
        authorize: AuthJWT = Depends(),
        db: Session = Depends(get_db)
):
    db_user = get_user_by_login(db, login=user.login)
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")

    if not db_user.check_password(user.password):
        raise HTTPException(status_code=401, detail="Bad username or password")

    # Use create_access_token() and create_refresh_token() to create our
    # access and refresh tokens
    return {
        "access_token": authorize.create_access_token(subject=db_user.id),
        "refresh_token": authorize.create_refresh_token(subject=db_user.id)
    }


@router.post('/refresh')
def refresh(authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    authorize.jwt_refresh_token_required()

    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


"""
curl -X GET http://localhost/v1/auth/protected -H "Content-Type: application/json" -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImlhdCI6MTY0NTc3MzczMSwibmJmIjoxNjQ1NzczNzMxLCJqdGkiOiI5MTkwNWRjMy04M2VlLTRlNjItODFmZS1lMWQ0ZTdjNzhhYWYiLCJleHAiOjE2NDU3NzQ2MzEsInR5cGUiOiJhY2Nlc3MiLCJmcmVzaCI6ZmFsc2V9.SOM3i0wdHjRiXGuFgL-xKq-RwUcO1oe6wFmZ4nXGwB8"
"""


@router.get('/protected')
def protected(authorize: AuthJWT = Depends()):
    authorize.jwt_required()

    user_id = authorize.get_jwt_subject()
    return {"user_id": user_id}
