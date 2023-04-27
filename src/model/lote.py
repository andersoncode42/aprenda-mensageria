import json

class Lote:

    def __init__(self, id_lote, id_categoria, lista_processo):
        """Definir o construtor da classe que recebe as propriedades como parâmetros"""
        # Atribua os valores dos parâmetros às propriedades da classe
        self.id_lote = id_lote
        self.id_categoria = id_categoria
        self.lista_processo = lista_processo

    def tojsontxt(self):
        """Retorna uma string json que representa as propriedades e valores do objeto python

        Returns:
            str: uma string json
        """

        # Criar um dicionário python com as propriedades e valores do objeto
        dicionario = {
            "id_lote": self.id_lote,
            "id_categoria": self.id_categoria,
            "lista_processo": self.lista_processo
        }

        # Converter o dicionário python em uma string json
        txt = json.dumps(dicionario)

        return txt

    def tobytes(self):
        """Retorna a string Json Serializada

        Returns:
            bytes: um objeto bytes que representa a string json
        """
        return self.tojsontxt().encode()
