from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Users(Base):
    __tablename__ = "Users"

    id: int = Column(Integer, primary_key=True, index=True)
    login: str = Column(String, unique=True, index=True, nullable=False, default="")
    hashed_password: str = Column(String, unique=False, index=True, nullable=False, default="")
    is_active: bool = Column(Boolean, default=True)

