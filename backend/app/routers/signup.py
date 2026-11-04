from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database_connect.make_engine import get_db
from app.schemas.users import Signup, SignupResponse
from app.repositories.user_auth import Repo_userSignup

signupRouter = APIRouter(prefix="/signup", tags=["signup"])


@signupRouter.post("/", response_model=SignupResponse)
async def user_signup(
            data: Signup,
            session: AsyncSession = Depends(get_db)
        ):

    return await Repo_userSignup(session, data)