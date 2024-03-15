from ..modules.Project.project_schema import Project
from pydantic import BaseModel

class ProjectInterface(BaseModel):
    user: Project 

