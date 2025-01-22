#!/bin/bash
cd /home/ubuntu/production
echo "remove old images"
sudo docker image rm 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-postgres:latest
sudo docker image rm 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-nginx:latest
sudo docker image rm 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-django:latest
echo "login ECR"
sudo aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 298325099374.dkr.ecr.us-east-1.amazonaws.com
echo "Pull latest images from ECR"
sudo docker image pull 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-postgres:latest
sudo docker image pull 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-django:latest
sudo docker image pull 298325099374.dkr.ecr.us-east-1.amazonaws.com/macroseat-nginx:latest
