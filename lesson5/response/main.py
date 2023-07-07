from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="lesson5/response/templates")



@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("item.html", {"request": request, "name": name})

@app.get("/html/")
async def read_root():
    return HTMLResponse("<h2>Hello World</h1>")


@app.get("/json/")
async def read_root():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)

