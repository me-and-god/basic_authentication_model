


from fastapi import HTTPException
from sqlalchemy import select

from app.auth.security import hash_password, verify_password
from app.models.users import User
from app.auth.token import create_access_token


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





async def Repo_UserLogin(
            data,
            session
    ):

    # first check using the email for login if the user for this email exist
    result = await session.execute(
        select(User).where(User.email == data.email)
    )

    user =  result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")


    # if the user exist verify the user input password with the user for the email 
    verified = verify_password(data.password, user.hashed_password)

    if not verified:
        raise HTTPException(status_code=400, detail="wrong credentials")


    # if done verified then issue the user an access token 
    access_token = create_access_token(user_id=user.id)

    return {
        "user": user,
        "token": access_token
    }



    