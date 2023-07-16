from pydantic import BaseModel, Field, EmailStr



class UserBase(BaseModel):
    name: str = Field(..., max_length=32)
    email: EmailStr = Field(...)


class UserIn(UserBase):
    password: str = Field(..., min_length=8, max_length=100)


class UserOut(UserBase):
    id: int
