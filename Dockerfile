FROM python:3.10.4-bullseye

ARG ENV
ARG PROJECT_DIR
ARG SRC_DIR

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

RUN mkdir $PROJECT_DIR
COPY ./bin $PROJECT_DIR/
RUN chmod +x $PROJECT_DIR/start_reload.sh $PROJECT_DIR/prestart.sh

WORKDIR $PROJECT_DIR/$SRC_DIR/

COPY ./src/poetry.lock ./src/pyproject.toml $PROJECT_DIR/$SRC_DIR/
RUN poetry install $(if [ "$ENV" = 'production' ]; then echo '--no-dev'; fi)

COPY ./src $PROJECT_DIR$SRC_DIR/
