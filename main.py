from fastapi import FastAPI, Request
from typing import List
from pydantic import BaseModel, Field
from starlette.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str = Field(None, title="name of student", max_length=10)
    subjects: List[str] = []


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post("/students/")
async def student_data(s1: Student):
    return s1


@app.get("/hello/")
async def hello():
    ret = '''
        <html>
        <body>
        <h2>Hello World!</h2>
        </body>
        </html>
        '''
    return HTMLResponse(content=ret)


@app.get("/hello/with_template/{name}", response_class=HTMLResponse)
async def hello(request: Request, name: str):
    return templates.TemplateResponse("hello.html", {"request": request, "name": name})
