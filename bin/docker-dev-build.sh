#!/bin/bash

image_name="smoke-image"

#docker rmi -f "$image_name"

docker build -t "$image_name" -f docker/Dockerfile .
