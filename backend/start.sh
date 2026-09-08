#!/bin/sh

set -e

if [ ! -f /run/secrets/database.env ]; then
    echo "Database secret file not found."
    exit 1
fi

set -a
. /run/secrets/database.env
set +a

if [ -z "$DATABASE_URL" ]; then
    echo "DATABASE_URL is not configured."
    exit 1
fi

exec uvicorn app.main:app --host 0.0.0.0 --port 8000
