from pydantic import BaseModel


class UserScheme(BaseModel):
    login: str
    password: str
