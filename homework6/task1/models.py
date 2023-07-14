from pydantic import BaseModel, Field, EmailStr
from datetime import date


class UserBase(BaseModel):
    firstname: str = Field(..., min_length=2, max_length=32)
    lastname: str = Field(..., min_length=2, max_length=32)
    email: EmailStr = Field(...)


class UserIn(UserBase):
    password: str = Field(..., min_length=8, max_length=100)


class UserOut(UserBase):
    id: int
