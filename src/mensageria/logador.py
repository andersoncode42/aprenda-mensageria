import logging


class Logador:
    """Classe responsável por fornecer recursos de log"""
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("pika").setLevel(logging.WARNING)

    @staticmethod
    def error(msg, excecao=None):
        """Envia uma mensagem de log do tipo error"""
        logger = logging.getLogger(__name__)

        if isinstance(excecao, Exception):
            exc_info = (type(excecao), excecao, excecao.__traceback__)
            logger.error(msg, exc_info=exc_info)
        else:
            logger.error(msg)

    @staticmethod
    def info(msg, excecao=None):
        """Envia uma mensagem de log do tipo info"""
        logger = logging.getLogger(__name__)

        if isinstance(excecao, Exception):
            exc_info = (type(excecao), excecao, excecao.__traceback__)
            logger.info(msg, exc_info=exc_info)
        else:
            logger.info(msg)

