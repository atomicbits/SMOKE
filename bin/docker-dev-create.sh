#!/bin/bash

WORK=$(pwd)
MODELS="$WORK/models"

image_name="smoke-image"
container_name="smoke-container"
jupyter_external_port="8688"

docker rm "$container_name" 
# --gpus=all
docker create  --name "$container_name" --gpus '"device=1"' -p "$jupyter_external_port":8888  -v $WORK:/work -v $MODELS:/home/appuser/.torch/models "$image_name"
