#!/bin/bash

DB_NAME=macroseat

echo "###";
echo "# Create DB if not exists";
echo "###";

psql postgres -U postgres -f /create_db.sql
