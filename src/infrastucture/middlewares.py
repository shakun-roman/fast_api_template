import uuid

from loguru import logger


async def request_id_middleware(request, call_next):
    request_id = str(uuid.uuid4())
    with logger.contextualize(request_id=request_id):
        logger.info("Request started")
        try:
            response = await call_next(request)
        except Exception as ex:
            logger.error(f"Request failed: {ex}")
        finally:
            response.headers["X-Request-ID"] = request_id
            logger.info("Request ended")
            return response
