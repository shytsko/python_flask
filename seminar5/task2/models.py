from enum import StrEnum
from pydantic import BaseModel
from typing import Optional


class Genre(StrEnum):
    biography = 'биографии'
    action = 'боевики'
    war = 'военные'
    comedy = 'комедии'
    historical = 'исторические'
    romance = 'мелодрама'


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: list[Genre]
