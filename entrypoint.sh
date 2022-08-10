#! /usr/bin/env bash

# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head
# Start uWSGI
exec uwsgi --ini config.ini
