from pydantic import BaseModel


class PostScheme(BaseModel):
    text: str


class PostId(BaseModel):
    post_id: int
