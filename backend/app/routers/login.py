from app.database_connect.make_engine import get_db
from app.schemas.users import Login, LoginResponse
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_auth import Repo_UserLogin

LoginRouter = APIRouter(prefix="/login", tags=["login"])


@LoginRouter.post("/", response_model=LoginResponse)
async def user_login(
    data: Login,
    session: AsyncSession = Depends(get_db)
):

    Result = await Repo_UserLogin(data, session)

    userData =  LoginResponse(
            name=Result["user"].name,
            email=Result["user"].email,
            token=Result["token"]
        )

    return userData
    


    