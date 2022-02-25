from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from pathlib import Path
from os import environ


class Settings(BaseModel):
    DATABASE_URL: str = environ.get('DATABASE_URL', 'sqlite://db.sqlite')
    BASE_DIR: str = Path(__file__).parent.parent.parent
    authjwt_secret_key: str = "971da3fe036ced8471c447ff0da3ef24c8be4f2f7673396a"


@AuthJWT.load_config
def AuthJWT_get_config() -> Settings:
    return Settings()


def get_config() -> Settings:
    return Settings()
