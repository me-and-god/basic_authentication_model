from pydantic import BaseModel, EmailStr


class Signup(BaseModel):
    name: str
    email: EmailStr
    password: str


class Login(BaseModel):
    email: EmailStr
    password: str

class SignupResponse(BaseModel):
    name: str
    email: str
    status: str = "Welcome ! Your account has been created."


class LoginResponse(BaseModel):
    name: str
    email: str
    token: str

