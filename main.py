#webserver with ibterface build on fast api
import os
from typing import Union
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse, JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from binance_api import get_curancy_data
from json import JSONDecoder
from enum import Enum
from typing import Tuple
from validation_form import User

app = FastAPI()
templates = Jinja2Templates(directory="static/templates")
# app.mount("/static", StaticFiles(directory="./static"), name="static")

folder = os.path.dirname(__file__)
app.mount("/static", StaticFiles(directory=folder+"\static", html=True, check_dir=True), name="static")


class user():
    name: str
    password: str
    email: str
    
        


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
    
    return templates.TemplateResponse('index.html', {"request": request})
    

# endpoint for main.html
@app.get("/registration", response_class=FileResponse, response_model=User)
async def registration(request: Request):
    
    return templates.TemplateResponse('registration.html', {"request": request})

@app.post("/submit_registration_form")
async def submit_registration_form(request: Request, username: str = Form(...), password: str = Form(...)):
    
    
    return templates.TemplateResponse('index.html', {"request": request}) 
    
    
