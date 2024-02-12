from datetime import datetime
from typing import Tuple
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    password: str 
    email: str
    registration_date: datetime
    
    
    
    
    
    
    