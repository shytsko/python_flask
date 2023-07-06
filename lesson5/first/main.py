from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'msg': 'Hello World!'}


@app.get('/items/{id}')
async def get_items(id: int, q: int = None):
    return {'id': id, 'q': q}
