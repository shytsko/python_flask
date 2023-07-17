# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трех таблиц: товары,
# заказы и пользователи.
# Таблица товары должна содержать информацию о доступных товарах, их описаниях и ценах.
# Таблица пользователи должна содержать информацию о зарегистрированных пользователях магазина.
# Таблица заказы должна содержать информацию о заказах, сделанных пользователями.
# ○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия,
#    адрес электронной почты и пароль.
# ○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
# ○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY),
#    id товара (FOREIGN KEY), дата заказа и статус заказа.
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой
# из трёх таблиц (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление

from fastapi import FastAPI
from user import user_router
from good import good_router
from order import order_router
from services import service_router
from db import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(service_router, tags=["Service"])
app.include_router(user_router, tags=["User"])
app.include_router(good_router, tags=["Good"])
app.include_router(order_router, tags=["Order"])
