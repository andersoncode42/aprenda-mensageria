#!/bin/bash

# set -x

#IMAGEM="rabbitmq:management"
IMAGEM="rabbitmq:3.11.14-management-alpine"
CONTAINER="pernalonga"

./container.up.sh "$IMAGEM" "$CONTAINER" \
&& sleep 10 \
&& ./rabbitmq.config.sh "$CONTAINER"