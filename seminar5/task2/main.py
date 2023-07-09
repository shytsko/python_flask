# Создать API для получения списка фильмов по жанру. Приложение должно иметь возможность получать
# список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.
import random

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .models import Movie, Genre

app = FastAPI()

Movies = [
    Movie(id=i,
          title=f'Movie {i}',
          description=f'description movie {i}',
          genre=random.sample(list(Genre), 3))
    for i in range(10)
]


@app.get('/movie/{genre}', response_model=list[Movie])
async def get_movies(genre: Genre):
    result = list(filter(lambda m: genre in m.genre, Movies))
    if not result:
        raise HTTPException(status_code=404, detail="Not Found")
    return result
