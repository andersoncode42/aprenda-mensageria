from enum import Enum
from logador import Logador
import pika
from pika.exceptions import AMQPError


class Conector:
    """Classe que provê informações / recursos para se conectar à mensageria"""

    # Credencias para se conectar
    MENSAGERIA_HOST = "localhost"
    MENSAGERIA_USUARIO = "guest"
    MENSAGERIA_SENHA = "guest"

    # Dados da Exchange
    EXCHANGE_NOME = "roteador"
    EXCHANGE_TIPO = "topic"

    class Fila(Enum):
        """Filas e suas respectivas routing keys"""
        PENDENTES = "PENDENTES"
        CONCLUIDOS = "CONCLUIDOS"
        ERROS = "ERROS"

    def getchannel(self):
        """Cria uma conexão com a mensageria e retorna um objeto dot tipo Canal Bloqueante
            Returns:
                (BlockingChannel): Um canal do RabbitMQ
        """

        try:
            credenciais = pika.PlainCredentials(self.MENSAGERIA_USUARIO, self.MENSAGERIA_SENHA)

            conexao = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.MENSAGERIA_HOST, credentials=credenciais)
            )

            canal = conexao.channel()

            # Declarar um exchange do tipo topic chamado "roteador"
            canal.exchange_declare(exchange=self.EXCHANGE_NOME,
                                   exchange_type=self.EXCHANGE_TIPO)

            return canal
        except Exception as excecao:
            Logador.error("Erro inesperado ao criar canal", excecao)

    def publique(self, msg, fila):
        """Publica a mensagem na fila
            Parameters:
                msg (str): A mensagem a ser publicada
                fila (str): O nome da fila
        """

        canal = self.getchannel()

        try:
            print(f"Tentando enviar a mensagem: {msg}, para a rota: {fila}")

            # Publicar uma mensagem no exchange com a routing key correspondente ao status
            canal.basic_publish(exchange=self.EXCHANGE_NOME,
                                routing_key=fila,
                                body=msg)

            # Registrar uma mensagem de sucesso
            Logador.info("Mensagem enviada com sucesso")

        except pika.exceptions.AMQPError as excecao:
            # Registrar uma mensagem de erro em caso de exceção do rabbitmq
            Logador.error("Erro AMQP", excecao)

        except Exception as excecao:
            # Registrar uma mensagem de erro em caso de qualquer outra exceção
            Logador.error("Erro inesperado ao enviar mensagem", excecao)
        finally:
            # Lembre-se de liberar / fechar o recurso
            canal.close()

    def consome(self, fila):
        """Retorna a mansagem da fila
            Parameters:
                fila (str): O nome da fila
            Returns:
                (str): A mensagem da fila
        """

        canal = self.getchannel()
        try:
            metodo, propriedades, msg = canal.basic_get(queue=fila, no_ack=True)
            return msg
        except Exception as excecao:
            Logador.error(f"Erro inesperado ao consumir mensagem da fila: {fila}", excecao)
        finally:
            # Sempre se lembre de liberar / fechar o recurso
            canal.close()