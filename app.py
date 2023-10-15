from typing import Union
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def derangement(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (derangement(n - 1) + derangement(n - 2))



@app.get("/")
def home_page(response_class=HTMLResponse):
    with open("templates/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/program")
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})

@app.post("/calculate")
def calculate(request: Request, n: int = Form(...)):
    result = derangement(n)
    return templates.TemplateResponse("form.html", {"request": request, "result": result, 'n': n})


# uvicorn app:app --reload
