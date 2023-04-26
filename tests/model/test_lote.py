# Importar o módulo unittest
import unittest
# Importar o módulo lote que contém a classe Lote
from src.model import lote

# Definir uma classe de teste que herda da classe TestCase
class TestLote(unittest.TestCase):
    # Definir um método de teste que verifica se o construtor da classe Lote atribui os valores corretos às propriedades
    def test_init(self):
        # Criar uma instância da classe Lote com valores arbitrários
        lote1 = lote.Lote(1, 2, [3, 4, 5])
        # Usar asserções para verificar se as propriedades do objeto têm os valores esperados
        self.assertEqual(lote1.id_lote, 1)
        self.assertEqual(lote1.id_categoria, 2)
        self.assertEqual(lote1.lista_processo, [3, 4, 5])

    # Definir um método de teste que verifica se o método get_json da classe Lote retorna um objeto json válido
    def test_get_json(self):
        # Criar uma instância da classe Lote com valores arbitrários
        lote1 = lote.Lote(1, 2, [3, 4, 5])
        # Chamar o método get_json para obter o objeto json
        objeto_json = lote1.get_json()
        # Usar asserções para verificar se o objeto json é uma string válida e tem o formato esperado
        self.assertIsInstance(objeto_json, str)
        self.assertEqual(objeto_json, '{"id_lote": 1, "id_categoria": 2, "lista_processo": [3, 4, 5]}')

    # Definir um método de teste que verifica se o método imprime_json da classe Lote imprime o objeto json na tela
    def test_imprime_json(self):
        # Criar uma instância da classe Lote com valores arbitrários
        lote1 = lote.Lote(1, 2, [3, 4, 5])
        # Usar o módulo io para capturar a saída do método imprime_json
        import io
        import sys
        output = io.StringIO()
        sys.stdout = output
        # Chamar o método imprime_json para imprimir o objeto json na tela
        lote1.imprime_json()
        # Restaurar a saída padrão
        sys.stdout = sys.__stdout__
        # Usar asserções para verificar se a saída capturada é igual ao objeto json esperado
        self.assertEqual(output.getvalue(), '{"id_lote": 1, "id_categoria": 2, "lista_processo": [3, 4, 5]}\n')

# Executar os testes usando o módulo unittest
if __name__ == "__main__":
    unittest.main()
