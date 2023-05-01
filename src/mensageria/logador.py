import logging


class Logador:
    """Classe responsável por fornecer recursos de log"""
    logging.basicConfig(level=logging.INFO)

    @staticmethod
    def error(msg, excecao=None):
        """Envia uma mensagem de log do tipo error"""
        logger = logging.getLogger(__name__)
        logger.error(msg, excecao)

    @staticmethod
    def info(msg, excecao=None):
        """Envia uma mensagem de log do tipo info"""
        logger = logging.getLogger(__name__)
        logger.info(msg, excecao)
