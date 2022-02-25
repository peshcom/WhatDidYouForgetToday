from sqlalchemy.orm import Session

from ..database.models import Users
from ..schemas.user import User


def get_user(db: Session, user_id: int) -> Users:
    return db.query(Users).filter(Users.id == user_id).first()


def get_user_by_login(db: Session, login: str) -> Users:
    return db.query(Users).filter(Users.login == login).first()


def create_user(db: Session, user: User) -> Users:
    db_user = Users(login=user.login)
    db_user.set_password(user.password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
