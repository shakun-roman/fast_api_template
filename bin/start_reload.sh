#!/usr/bin/env sh
set -e

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8111}
LOG_LEVEL=${LOG_LEVEL:-info}

PRE_START_PATH=./prestart.sh

echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else
    echo "There is no script $PRE_START_PATH"
fi

exec uvicorn $(test ${ENV} = development && echo "--reload") --host $HOST --port $PORT --log-level $LOG_LEVEL --app-dir $PROJECT_DIR$SRC_DIR app:app
