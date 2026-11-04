


from fastapi import HTTPException
from sqlalchemy import select

from app.auth.security import hash_password
from app.models.users import User


async def Repo_userSignup(
        session,
        data
):
    exist = await session.scalar(
        select(select(User.id).where(User.email == data.email).exists())
    )
    if exist:
        raise HTTPException(
            status_code=401,
            detail="This email is already taken , Try another another email"
        )
    
    PwdHash = hash_password(data.password)
    user = User(name=data.name, email=data.email, hashed_password=PwdHash)

    session.add(user)

    await session.commit()

    return user
