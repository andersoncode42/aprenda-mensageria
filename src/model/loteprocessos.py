import json


class LoteProcessos:

    def __init__(self, idlote, idcategoria, lista_de_processos):
        """Construtor da classe que recebe as propriedades como parâmetros

            Parameters:
                idlote (int): O id do lote de processos
                idcategoria (int): O id que representa a categoria dos processos
                lista_de_processos (list): Uma lista de processos
        """
        # Atribua os valores dos parâmetros às propriedades da classe
        self.idlote = idlote
        self.idcategoria = idcategoria
        self.lista_de_processos = lista_de_processos

    def tojsontxt(self):
        """Retorna uma string json que representa as propriedades e valores do objeto python

        Returns:
            str: uma string json
        """

        # Criar um dicionário python com as propriedades e valores do objeto
        dicionario = {
            "idlote": self.idlote,
            "idcategoria": self.idcategoria,
            "lista_de_processos": self.lista_de_processos
        }

        # Converter o dicionário python em uma string json
        txt = json.dumps(dicionario)

        return txt

    def tobytes(self):
        """Retorna a string Json Serializada(bytes)

        Returns:
            bytes: um objeto bytes que representa a string json
        """
        return self.tojsontxt().encode()
