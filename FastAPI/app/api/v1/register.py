from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from ...crud.users import create_user
from ...schemas.user import UserScheme

router = APIRouter(
    prefix="/register",
    tags=["register"],
    responses={404: {"description": "Not found"}},
)

"""
curl -X POST http://localhost/v1/register/ -H "Content-Type: application/json" -d '{"login":"user3","password":"password"}'
"""


@router.post('/')
def index(user: UserScheme, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
