from fastapi import APIRouter, HTTPException, status
from passlib.context import CryptContext
from db import users, database
from models import UserIn, UserOut

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
user_router = APIRouter()


@user_router.get("/users", response_model=list[UserOut])
async def get_all_users():
    query = users.select()
    return await database.fetch_all(query)


@user_router.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user


@user_router.post("/users", response_model=UserOut)
async def create_user(new_user: UserIn):
    new_user.password = pwd_context.hash(new_user.password)
    query = users.insert().values(**new_user.dict())
    last_record_id = await database.execute(query)
    query = users.select().where(users.c.id == last_record_id)
    return await database.fetch_one(query)


@user_router.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, new_user: UserIn):
    new_user.password = pwd_context.hash(new_user.password)
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@user_router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    res = await database.execute(query)
    if res > 0:
        return {'message': 'User deleted'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
