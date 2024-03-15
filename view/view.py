from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastui import prebuilt_html

router = APIRouter()


@router.get("/") #/api
async def root() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='Demo'))