#!/bin/bash

WORK=$(pwd)

image_name="smoke-image"
container_name="smoke-container"
jupyter_external_port="8688"

docker rm "$container_name" 
docker create  --name "$container_name" --gpus=all -p "$jupyter_external_port":8888  -v $WORK:/work "$image_name"
