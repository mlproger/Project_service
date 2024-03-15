from fastapi import APIRouter
from fastui import AnyComponent
from fastui.components import Page, Heading, Div, Button
from fastui.events import GoToEvent

router = APIRouter(prefix = "/api")

@router.get("/", response_model_exclude_none=True)
def root() -> list[AnyComponent]:
    return [
        Page(
            components = [
                Heading(
                    text="Привествую!", 
                    level=1,
                    class_name="position-absolute start-50 translate-middle"
                ),
                Heading(
                    text="Это мой небольшой проект, суть которого заключается в создании системы управления проектами", 
                    class_name='pt-5',
                    level=4
                ),
                Heading(
                    text="Стек технологий: FastAPI, FastUI", 
                    class_name='pt-5',
                    level=4
                ),
                Div(
                    components = [
                        Button(
                            text = "Начать", 
                            class_name="btn btn-primary btn-lg",
                            on_click=GoToEvent(url='/user'),
                        )
                    ],

                    class_name = "position-absolute top-50 start-50 translate-middle"
                )
            ]
        )
    ]