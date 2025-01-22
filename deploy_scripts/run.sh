#!/bin/bash
cd /home/ubuntu/production
echo "Starting server..."
sudo -E docker compose -f ./docker-compose-prod-codedeploy.yml up -d
echo "Starting server done"