from fastapi import Body, FastAPI, Request
from fastapi.responses import JSONResponse
from core.exseption import MyExseption
from server.user_api import router as user_router
from view.view import router as view_router
from server.main_api import router as main_router

app = FastAPI()
app.include_router(main_router)
app.include_router(user_router)
app.include_router(view_router)




@app.exception_handler(MyExseption)
async def my_exception(req: Request, exc: MyExseption):
    return JSONResponse(
        status_code = exc.status_code,
        content = {
            "status_code": exc.status_code,
            "msg": exc.msg
        }
    )

