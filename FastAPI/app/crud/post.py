from sqlalchemy.orm import Session

from ..database.models import Posts
from ..schemas.post import PostScheme


def get_posts(db: Session, user_id: int) -> Posts:
    return db.query(Posts).filter(Posts.user_id == user_id).all()


def create_post(db: Session, post: PostScheme, user_id: int) -> Posts:
    db_post = Posts(
        text=post.text,
        user_id=user_id,
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post
