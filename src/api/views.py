from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/healthcheck")
async def healthcheck():
    return JSONResponse(content={"status": "ok"}, status_code=200)
