from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .models import Task

app = FastAPI()

tasks = {i: Task(title=f'task{i}', description=f'description task {i}') for i in range(5)}


@app.get('/tasks/{task_id}', response_model=Task)
async def task_get(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Not Found")
    return tasks[task_id]


@app.get('/tasks', response_model=dict[int, Task])
async def task_get_all():
    return tasks


@app.post('/tasks')
async def task_post(task: Task):
    next_task_id = max(tasks.keys()) + 1
    tasks[next_task_id] = task
    return {'task_id': next_task_id, 'task': tasks[next_task_id]}


@app.put('/tasks')
async def task_put(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Not Found")
    tasks[task_id] = task
    return {'task_id': task_id, 'task': tasks[task_id]}


@app.delete('/tasks')
async def task_delete(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Not Found")
    tasks.pop(task_id)
    return JSONResponse({"detail": "Success"}, 200)
