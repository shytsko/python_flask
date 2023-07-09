# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.


from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .models import UserIn, UserOut

app = FastAPI()
templates = Jinja2Templates(directory="seminar5/task3/templates")

users = {i: UserIn(name=f'user{i}', email=f'email{i}@mail.com', password=f'password{i}') for i in range(5)}


@app.post('/users', response_model=UserOut)
async def user_post(new_user: UserIn):
    new_user_id = max(users.keys()) + 1
    users[new_user_id] = new_user
    return UserOut(id=new_user_id, name=new_user.name, email=new_user.email)


@app.put('/users', response_model=UserOut)
async def user_put(user_id: int, user: UserIn):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Not Found")
    users[user_id] = user
    return UserOut(id=user_id, name=user.name, email=user.email)


@app.delete('/users')
async def user_delete(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Not Found")
    users.pop(user_id)


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    users_list = [UserOut(id=k, name=v.name, email=v.email) for k, v in users.items()]
    return templates.TemplateResponse("users.html", {"request": request, "users": users_list, "title": "Пользователи"})
