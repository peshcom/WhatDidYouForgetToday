from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from pathlib import Path
from os import environ


class Settings(BaseModel):
    DATABASE_URL: str = environ.get('DATABASE_URL', 'sqlite://db.sqlite')
    BASE_DIR: str = Path(__file__).parent.parent.parent
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def AuthJWT_get_config() -> Settings:
    return Settings()


def get_config() -> Settings:
    return Settings()
