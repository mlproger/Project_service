from ..modules.User.user_schema import User
from pydantic import BaseModel



class UserInterface(BaseModel):
    user: User 

    @staticmethod
    def get_public_information(user: User):
        if user.projects == None:
            user.projects = []
        return {
            "name": user.name,
            "project": user.projects
        }
    
    @staticmethod
    def get_private_information(user: User):
        return user.model_dump()

