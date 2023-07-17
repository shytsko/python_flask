# Разработать API для управления списком задач с использованием базы данных MongoDB.
# Для этого создайте модель Task со следующими полями:
# ○ id: str (идентификатор задачи, генерируется автоматически)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)
# API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели Task. Для работы с базой данных используйте PyMongo.
from fastapi import FastAPI
from task import task_router

app = FastAPI()

app.include_router(task_router, tags=["Task"])
