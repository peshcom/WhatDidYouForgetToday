from typing import AnyStr

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import bcrypt

from ..database import Base


class Users(Base):
    __tablename__ = "Users"

    id: int = Column(Integer, primary_key=True, index=True)
    login: str = Column(String, unique=True, index=True, nullable=False, default="")
    hashed_password: str = Column(String, unique=False, index=True, nullable=False, default="")
    is_active: bool = Column(Boolean, default=True)

    posts = relationship("Posts")

    def set_password(self, password: AnyStr):
        self.hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        return self.hashed_password

    def check_password(self, password: AnyStr):
        # Check hashed password. Using bcrypt, the salt is saved into the hash itself
        return bcrypt.checkpw(password.encode(), self.hashed_password.encode())
