import uuid
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Body
from fastui import AnyComponent
from fastui.components import Page, Heading
from core.exseption import MyExseption
from modules.User.user_schema import User, UserSchema


router = APIRouter(prefix = "/api/user")
db = None


@router.post("/add")
def add_user(body: dict = Body(...)):
    try:
        UserSchema.model_validate(body)

        user = UserSchema.model_validate(body)
        __id = uuid.uuid4()

        __user = User(
            name = user.name,
            user_id = str(__id)
        )

        db.add_user(__user)
        return JSONResponse(
            status_code=201,
            content = {
                "status":"OK"
            }
        )
    except ValueError:
        raise MyExseption(staus_code=400, msg="Пользователь с таким именем уже зарегистрирован")
    except:
        raise MyExseption(staus_code=400, msg="Неверный формат данных")



@router.get("/", response_model_exclude_none=True)
def get_user() -> list[AnyComponent]:
    return [
        Page(
            components = [
                Heading(
                    text="HELLO",
                    level=1
                )
            ]
        )
    ]