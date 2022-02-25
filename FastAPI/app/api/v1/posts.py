from fastapi import APIRouter
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from ...crud.post import create_post, get_posts
from ...database import get_db
from ...schemas.post import PostScheme

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


"""
curl -X GET http://localhost/v1/posts/ -H "Content-Type: application/json" -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIsImlhdCI6MTY0NTc3NjQ2NywibmJmIjoxNjQ1Nzc2NDY3LCJqdGkiOiI0ZjgwY2ZjNC04ZTc2LTRjYWUtYTQwYy1mNzRmOWM3NzEwNmQiLCJleHAiOjE2NDU3NzczNjcsInR5cGUiOiJhY2Nlc3MiLCJmcmVzaCI6ZmFsc2V9.dxBzdVBXVBS5WxuuzRI8nD-NZalknmn6r7nc3IZow1k"
"""


@router.get('/')
def index(
        db: Session = Depends(get_db),
        authorize: AuthJWT = Depends(),
):
    """
    Возвращает список постов для текущего пользователя
    """
    authorize.jwt_required()
    return get_posts(
        db=db,
        user_id=authorize.get_jwt_subject(),
    )


"""
curl -X POST http://localhost/v1/posts/ -d '{"text":"hello world2"}' -H "Content-Type: application/json" -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIsImlhdCI6MTY0NTc3NjQ2NywibmJmIjoxNjQ1Nzc2NDY3LCJqdGkiOiI0ZjgwY2ZjNC04ZTc2LTRjYWUtYTQwYy1mNzRmOWM3NzEwNmQiLCJleHAiOjE2NDU3NzczNjcsInR5cGUiOiJhY2Nlc3MiLCJmcmVzaCI6ZmFsc2V9.dxBzdVBXVBS5WxuuzRI8nD-NZalknmn6r7nc3IZow1k"
"""


@router.post('/')
def new_post(
        post: PostScheme,
        db: Session = Depends(get_db),
        authorize: AuthJWT = Depends(),
):
    """
    Создает новый пост
    """
    authorize.jwt_required()
    return create_post(
        db=db,
        post=post,
        user_id=authorize.get_jwt_subject(),
    )
