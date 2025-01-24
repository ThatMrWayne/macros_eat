#!/bin/bash
cd /home/ubuntu/production
echo "remove old images"
docker image rm 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-postgres:latest
docker image rm 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-nginx:latest
docker image rm 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-django:latest
echo "login ECR"
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 298325099374.dkr.ecr.us-east-1.amazonaws.com
echo "Pull latest images from ECR"
docker image pull 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-postgres:latest
docker image pull 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-django:latest
docker image pull 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-nginx:latest
