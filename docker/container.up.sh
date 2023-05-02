#!/bin/bash
# LEVANTA UMA INSTANCIA DO RABBITMQ NO LOCALHOST
# set -x

destroi_ambiente() {
    local img="$1"
    local ct="$2"

    echo "==AVISO======="
    echo "Removendo o container $ct"
    docker rm -f "$ct" &> /dev/null

    # echo "==AVISO======="
    # echo "Removendo a imagem $img"
    # docker image rm -f "$img" &> /dev/null
}

levanta_ambiente() {
    local img="$1"
    local ct="$2"

    echo "==AVISO======="
    echo "Rodando o container: $2 baseado na imagem: $1"
    docker run -d     \
    --name "$ct"      \
    --hostname "$ct"  \
    -p 5672:5672      \
    -p 15672:15672    \
    "$img"
}

# COMEÇA AQUI
IMAGEM="$1"
CONTAINER="$2"

destroi_ambiente "$IMAGEM" "$CONTAINER"
levanta_ambiente "$IMAGEM" "$CONTAINER"