import logging
import sys

from pathlib import Path

from loguru import logger
from settings.settings import settings


class InterceptHandler(logging.Handler):
    loglevel_mapping = {
        50: "CRITICAL",
        40: "ERROR",
        30: "WARNING",
        20: "INFO",
        10: "DEBUG",
        0: "NOTSET",
    }

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        log = logger.bind(request_id="app")
        log.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def init_logging():
    logger.remove()

    log_level = settings.LOG_LEVEL.upper()

    logger.add(
        sys.stdout,
        enqueue=True,
        backtrace=True,
        level=log_level,
        format=settings.LOG_FORMAT,
        serialize=settings.LOG_SERIALIZE,
    )
    logger.add(
        Path(settings.LOG_PATH) / settings.LOG_FILENAME,
        rotation=settings.LOG_ROTATION,
        retention=settings.LOG_RETENTION,
        enqueue=True,
        backtrace=True,
        level=log_level,
        format=settings.LOG_FORMAT,
        serialize=settings.LOG_SERIALIZE,
    )
    logging.basicConfig(handlers=[InterceptHandler()], level=0)

    for uvicorn_loger in ("uvicorn", "uvicorn.access", "uvicorn.error"):
        logging.getLogger(uvicorn_loger).handlers.clear()
        logging.getLogger(uvicorn_loger).propagate = True

    logger.bind(request_id=None)
