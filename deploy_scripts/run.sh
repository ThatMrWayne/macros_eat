#!/bin/bash
cd /home/ubuntu/production
echo "Starting server..."
docker compose -f ./docker-compose-prod-codedeploy.yml up -d
