from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: str
    done: bool


class TaskIn(TaskBase):
    pass


class TaskOut(TaskBase):
    _id: str


class TaskUpdate(BaseModel):
    title: str | None
    description: str | None
    done: bool | None
