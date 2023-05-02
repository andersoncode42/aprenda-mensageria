#!/bin/bash

# set -x

mostrelog() {
    local ct="$1"
    local qtdlinhas=2

    echo "==LOG======="
    docker logs "$ct" --tail="$qtdlinhas"
}

execute() {
    # Dentro do container, execute o comando
    local ct="$1"
    local cmd="$2"

    echo "==AVISO======="
    echo "CONTAINER: $ct"
    echo "COMANDO: $cmd"

    comando_completo="docker exec -d $ct $cmd"
    #saida_comando=$($comando_completo)
    echo "Comando Completo: $comando_completo"
    #echo "Saída Comando: $saida_comando"
}

# A lógica começa aqui
CONTAINER="$1"
EXCHANGE="ROTEADOR"
FILAS=("PENDENTES" "CONCLUIDOS" "ERROS")

echo "#==AVISO=============="
echo "# Habilitando Plugins "
# execute "$CONTAINER" "rabbitmq-plugins enable rabbitmq_management"
docker exec -d "$CONTAINER" rabbitmq-plugins enable rabbitmq_management
mostrelog "$CONTAINER"

# execute "$CONTAINER" "rabbitmqctl add_vhost $vhost";
# mostrelog "$CONTAINER"

echo "#==AVISO=============="
echo "# Criando Exchange    "
# execute "$CONTAINER" "rabbitmqadmin declare exchange --vhost='/' name='ROTEADOR' type='topic'"
docker exec -d "$CONTAINER" rabbitmqadmin                \
                            declare exchange --vhost='/' \
                            name="$EXCHANGE"             \
                            type='topic'
mostrelog "$CONTAINER"


for fila in "${FILAS[@]}"; do

    echo "#==AVISO=============="
    echo "# Criando as Filas    "
    docker exec -d "$CONTAINER" rabbitmqadmin  \
                    declare queue --vhost='/'  \
                    name="$fila"               \
                    durable='true'
    mostrelog "$CONTAINER"

    echo "#==AVISO=============="
    echo "# Bindando as Filas   "
    echo "# com a exchange      "
    docker exec -d "$CONTAINER" rabbitmqadmin   \
                    declare binding             \
                    --vhost='/'                 \
                    source="$EXCHANGE"          \
                    destination_type='queue'    \
                    destination="$fila"         \
                    routing_key="$fila"
    mostrelog "$CONTAINER"

done