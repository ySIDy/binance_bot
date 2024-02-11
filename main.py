#webserver with ibterface build on fast api
import os
from typing import Union
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse, JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from binance_api import get_curancy_data

app = FastAPI()
templates = Jinja2Templates(directory="static/templates")
# app.mount("/static", StaticFiles(directory="./static"), name="static")

folder = os.path.dirname(__file__)
app.mount("/static", StaticFiles(directory=folder+"\static", html=True, check_dir=True), name="static")

# @app.get("/")
# def reed_root():
#     return {"1": 1}

@app.get("/data_json/")
async def get_json_data():
    return get_curancy_data(symbol='BNBBTC')

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/", response_class=RedirectResponse)
async def reed_root():
    return RedirectResponse("main")

@app.get("/main", response_class=FileResponse)
async def main_page(request: Request):
    # update and return response without buffer
    # return JSONResponse(get_curancy_data(symbol='BNBBTC'))
    
    # data return
    # return get_curancy_data(symbol='BNBBTC')
    
    # page return
    return templates.TemplateResponse('index.html', {"request": request})
    return FileResponse("static/template/index.html")

# endpoint for main.html
@app.get("/registration", response_class=FileResponse)
async def registration():
    return FileResponse("registration.html")

@app.post("/submit_form")
async def submit_form(username: str = Form(...), password: str = Form(...)):
    
    # form procesing logic
    return {"username": username, "password": password}
