#!/bin/sh
# Clean up containers
sudo docker stop $(sudo docker ps -a -q) > /dev/null 2>&1
sudo docker rm $(sudo docker ps -a -q) > /dev/null 2>&1