from fastapi import APIRouter

from . import auth
from . import register
from . import posts

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    responses={404: {"description": "Not found"}},
)

router.include_router(auth.router)
router.include_router(register.router)
router.include_router(posts.router)

