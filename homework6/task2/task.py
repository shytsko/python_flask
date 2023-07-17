from fastapi import APIRouter, HTTPException, status
from models import TaskIn, TaskOut, TaskUpdate
from db import tasks

task_router = APIRouter()


# @task_router.get("/tasks", summary="Get all tasks", response_model=list[TaskOut])
# async def get_all_tasks():
#     pass
#
#
# @task_router.get("/tasks/{task_id}", summary="Get task by id", response_model=TaskOut)
# async def get_task(task_id: str):
#     pass


@task_router.post("/tasks", summary="Create new task", response_model=TaskOut)
async def create_task(new_task: TaskIn):
    try:
        result = tasks.insert_one(new_task.dict(exclude_none=True))
        new_task = tasks.find_one({'_id': result.inserted_id})
        print(new_task)
        return new_task
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Что-то пошло не по плану")


# @task_router.put("/tasks/{task_id}", summary="Update task", response_model=TaskOut)
# async def update_task(task_id: str, update_task_data: TaskUpdate):
#     pass
#
#
# @task_router.delete("/tasks/{task_id}", summary="Delete user")
# async def delete_user(task_id: int):
#     pass
