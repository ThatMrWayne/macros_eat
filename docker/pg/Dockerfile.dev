FROM postgres:16

# Set work directory
WORKDIR /

COPY docker/db-init-scripts/ docker-entrypoint-initdb.d/
COPY docker/scripts/create_db.sql create_db.sql
