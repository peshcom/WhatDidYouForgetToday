from fastapi import APIRouter

from . import auth

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    responses={404: {"description": "Not found"}},
)

router.include_router(auth.router)

