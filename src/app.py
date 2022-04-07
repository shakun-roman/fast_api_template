from api.views import router
from fastapi import FastAPI
from infrastucture.middlewares import request_id_middleware
from settings.log_settings import init_logging
from settings.settings import settings


def create_app():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        openapi_url=settings.OPENAPI_URL,
        debug=settings.DEBUG,
    )
    init_logging()

    app.middleware("http")(request_id_middleware)

    app.include_router(router, prefix=settings.API_V1_URL)

    return app


app = create_app()
