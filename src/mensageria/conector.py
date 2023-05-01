# pip install pika
# pip install logging

from enum import Enum
import pika
from pika.exceptions import AMQPError
from logador import Logador


class Conector:
    """Classe que contém provê informação/recursos para se conectar à mensageria"""

    # Credencias para se conectar
    MENSAGERIA_HOST = "localhost"
    MENSAGERIA_USUARIO = "guest"
    MENSAGERIA_SENHA = "guest"

    # Dados da Exchange
    EXCHANGE_NOME = "roteador"
    EXCHANGE_TIPO = "topic"

    # Dados das filas associadas À exchange
    class Fila(Enum):
        """Filas e suas respectivas routing keys"""
        PENDENTES = "p"
        CONCLUIDOS = "c"
        ERROS = "e"

    def getchannel(self):
        """Cria uma conexão com a mensageria e retorna um objeto dot tipo Canal Bloqueante
            Returns:
                (BlockingChannel): Um canal do RabbitMQ
        """
        credenciais = pika.PlainCredentials(self.MENSAGERIA_USUARIO, self.MENSAGERIA_SENHA)

        conexao = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.MENSAGERIA_HOST, credentials=credenciais)
        )

        canal = conexao.channel()

        # Declarar um exchange do tipo topic chamado "roteador"
        canal.exchange_declare(exchange=self.EXCHANGE_NOME,
                               exchange_type=self.EXCHANGE_TIPO)

        return canal

    def publique(self, msg, rota):
        """Método responsável por publicar a mensagem na Exchange"""

        canal = self.getchannel()

        try:
            print(f"Tentando enviar a mensagem: {msg}, para a rota: {rota}")

            # Publicar uma mensagem no exchange com a routing key correspondente ao status
            canal.basic_publish(exchange="roteador",
                                routing_key=rota,
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
            canal.close()

    def __init__(self):
        """Construtor da classe que recebe as propriedades como parâmetros

            Parameters:
                idlote (int): O id do lote de processos
                idcategoria (int): O id que representa a categoria dos processos
                lista_de_processos (list): Uma lista de processos
        """
        # Atribua os valores dos parâmetros às propriedades da classe
        pass

    @staticmethod
    def insira_pendente(self, lote_de_processos):
        """Insere na fila de Pendentes

        """
        # TODO document why this method is empty
        pass

    @staticmethod
    def insira_concluido(self, lote_de_processos):
        """Insere na fila de Concluídos

                """
        # TODO document why this method is empty
        pass

    @staticmethod
    def insira_erro(self, lote_de_processos):
        """Insere na fila de Erros

        """
        # TODO document why this method is empty
        pass