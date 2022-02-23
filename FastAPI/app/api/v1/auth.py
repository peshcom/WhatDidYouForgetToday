from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def index():
    return "auth"
