from pydantic import BaseModel
from typing import Optional

class Project(BaseModel):
    name: str 
    author: str 
    team: list = [author]