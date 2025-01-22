#!/bin/bash
cd /home/ubuntu/production
echo "Stop current containers"
sudo -E docker compose -f ./docker-compose-prod-codedeploy.yml down -v
echo "Stop current containers do