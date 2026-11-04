from datetime import datetime, timedelta, timezone

import jwt
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRY_MINUTES: int = 10

    model_config = SettingsConfigDict(
                                    env_file=".env",
                                    extra="ignore"
                                )



settings = Settings()  # type: ignore





# function to create a token and get that to the user logging in 

def create_access_token(
                        user_id: str
                ) -> str:

    expire_at = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRY_MINUTES)

    payload = {
                "sub": str(user_id),
                "exp": expire_at
            }


    return jwt.encode(
                    payload=payload,
                    key=settings.JWT_SECRET_KEY,
                    algorithm=settings.JWT_ALGORITHM
                )