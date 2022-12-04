#!/bin/bash

WORK=$(pwd)

image_name="smoke-image"
container_name="smoke-container"

#docker rm "$container_name" 
docker create  -it  --name "$container_name" --gpus=all -p 8886:8888  -v $WORK:/work "$image_name"
