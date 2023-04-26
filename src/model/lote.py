# Importar o módulo json para trabalhar com objetos json
import json

# Definir a classe Lote
class Lote:
    # Definir o construtor da classe que recebe as propriedades como parâmetros
    def __init__(self, id_lote, id_categoria, lista_processo):
        # Atribuir os valores dos parâmetros às propriedades da classe
        self.id_lote = id_lote
        self.id_categoria = id_categoria
        self.lista_processo = lista_processo

    # Definir o método get_json que retorna um objeto json que representa as propriedades e valores do objeto python
    def get_json(self):
        # Criar um dicionário python com as propriedades e valores do objeto
        dicionario = {
            "id_lote": self.id_lote,
            "id_categoria": self.id_categoria,
            "lista_processo": self.lista_processo
        }
        # Converter o dicionário python em um objeto json usando o módulo json
        objeto_json = json.dumps(dicionario)
        # Retornar o objeto json
        return objeto_json

    # Definir o método imprime_json que imprime o referido objeto json
    def imprime_json(self):
        # Chamar o método get_json para obter o objeto json
        objeto_json = self.get_json()
        # Imprimir o objeto json usando a função print
        print(objeto_json)