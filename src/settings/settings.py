from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "App"
    PROJECT_DESCRIPTION: str = "App desctiption."

    API_V1_URL: str = "/api/v1"
    OPENAPI_URL: str = f"{API_V1_URL}/openapi.json"

    # ENV VARS
    DEBUG: bool
    PROJECT_DIR: str
    SRC_DIR: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # DEFAULT ENV VARS
    LOG_LEVEL: str = "INFO"
    LOG_PATH: str = "/var/logs"
    LOG_FILENAME: str = "app.log"
    LOG_ROTATION: str = "20 days"
    LOG_RETENTION: str = "1 months"
    LOG_SERIALIZE: bool = False
    LOG_FORMAT: str = (
        "<level>{level: <8}</level> <green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> request id: {extra[request_id]} -"
        " <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
    )

    class Config:
        case_sensitive = True


settings: Settings = Settings()
