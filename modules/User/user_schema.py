from typing import Optional
from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError

#для сервера, бд и прочего
class User(BaseModel):
    name: str
    projects: Optional[list] = None
    user_id: str


#для возврата, создания и тд
class UserSchema(BaseModel):
    name: str = Field(...)


    