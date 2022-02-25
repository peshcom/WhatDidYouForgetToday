from sqlalchemy.orm import Session

from ..database.models import Posts
from ..schemas.post import PostScheme


def get_posts(db: Session, user_id: int) -> Posts:
    return db.query(Posts).filter(Posts.user_id == user_id).order_by(Posts.id.desc()).all()


def create_post(db: Session, post: PostScheme, user_id: int) -> Posts:
    db_post = Posts(
        text=post.text,
        user_id=user_id,
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


def delete_posts(db: Session, post_id: int, user_id: int) -> Posts:
    post = db.query(Posts).filter(Posts.id == post_id).first()
    if not post:
        raise ValueError("Post not found")
    if post.user_id != user_id:
        raise ValueError("You not have access to delete this entry")
    db.delete(post)
    db.commit()
