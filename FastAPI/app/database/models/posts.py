from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Posts(Base):
    __tablename__ = "Posts"

    id: int = Column(Integer, primary_key=True, index=True)
    text: str = Column(String, nullable=False, default="")
    user_id = Column(Integer, ForeignKey('Users.id'))
