from fastapi import Body
from fastapi.responses import JSONResponse





@app.post("/project/add/{name}")
def add_project(name: str, body: dict = Body(...)):
    if db.get_user_info_by_name(name) == []:
        raise MyExseption(staus_code=403, msg = "Пользователь не найден / не авторизирован")
    try:
        project_name = body["project_name"]
        project_author = name

        return JSONResponse(
            status_code=201,
            content = {
                "project_name": project_name,
                "project_author": project_author
            }
        )

    except Exception as e:
        print(e)
        raise MyExseption(staus_code=400, msg = "Неверный формат данных")


@app.get("/project/get")
def get_project():
    pass
