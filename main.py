#webserver with ibterface build on fast api
import os
from typing import Union
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="./static"), name="static")

folder = os.path.dirname(__file__)
app.mount("/main", StaticFiles(directory=folder+"\static", html=True, check_dir=True), name="static")

# @app.get("/")
# def reed_root():
#     return {"1": 1}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/", response_class=RedirectResponse)
async def reed_root():
    return RedirectResponse("main")

@app.get("/main", response_class=FileResponse)
async def main_page():
    return FileResponse("static/template/index.html")

# endpoint for main.html
@app.get("/registration", response_class=FileResponse)
async def registration():
    return FileResponse("registration.html")

@app.post("/submit_form")
async def submit_form(username: str = Form(...), password: str = Form(...)):
    
    # form procesing logic
    return {"username": username, "password": password}
