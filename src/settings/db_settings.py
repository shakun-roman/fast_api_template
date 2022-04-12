import databases
import sqlalchemy

from settings.settings import settings

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
