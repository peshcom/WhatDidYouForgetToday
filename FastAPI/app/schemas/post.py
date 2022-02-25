from pydantic import BaseModel


class PostScheme(BaseModel):
    text: str
