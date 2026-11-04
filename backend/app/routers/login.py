from fastapi import APIRouter

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/")
async def user_login()