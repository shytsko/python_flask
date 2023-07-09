from enum import IntEnum, auto
from pydantic import BaseModel
from typing import Optional


class TaskStatus(IntEnum):
    TO_DO = 0
    IN_PROCESS = 1
    DONE = 2


class Task(BaseModel):
    title: str
    description: Optional[str]
    status: TaskStatus = TaskStatus.TO_DO
