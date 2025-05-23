class Table:
    def __init__(self, headers):
        """Inicializa a tabela com cabeçalhos e linhas vazias"""
        self.headers = headers
        self.rows = []
    
    def add_row(self, row_data):
        """Adiciona uma nova linha à tabela"""
        if len(row_data) != len(self.headers):
            raise ValueError("Número de colunas não corresponde aos cabeçalhos")
        self.rows.append(row_data)
    
    def get_row(self, index):
        """Retorna uma linha específica pelo índice"""
        if index < 0 or index >= len(self.rows):
            raise IndexError("Índice da linha fora do intervalo")
        return self.rows[index]
    
    def remove_row(self, index):
        """Remove uma linha pelo índice"""
        if index < 0 or index >= len(self.rows):
            raise IndexError("Índice da linha fora do intervalo")
        return self.rows.pop(index)
    
    def display(self):
        """Exibe a tabela formatada (para visualização simples)"""
        print("| " + " | ".join(self.headers) + " |")
        print("-" * (sum(len(h) for h in self.headers) + 3 * len(self.headers) + 1))
        for row in self.rows:
            print("| " + " | ".join(str(item) for item in row) + " |")
    
    def search(self, column_name, value):
        """Busca linhas onde a coluna especificada contém o valor"""
        if column_name not in self.headers:
            raise ValueError("Coluna não encontrada nos cabeçalhos")
        col_index = self.headers.index(column_name)
        return [row for row in self.rows if row[col_index] == value]


import unittest

class TestTable(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.sample_headers = ["ID", "Nome", "Idade"]
        self.table = Table(self.sample_headers)
        
        # Adiciona algumas linhas de exemplo
        self.table.add_row([1, "Alice", 25])
        self.table.add_row([2, "Bob", 30])
        self.table.add_row([3, "Charlie", 35])
    
    def test_initialization(self):
        """Testa a inicialização da tabela"""
        self.assertEqual(self.table.headers, self.sample_headers)
        self.assertEqual(len(self.table.rows), 3)
    
    def test_add_row(self):
        """Testa a adição de novas linhas"""
        initial_row_count = len(self.table.rows)
        self.table.add_row([4, "David", 40])
        self.assertEqual(len(self.table.rows), initial_row_count + 1)
    
    def test_add_invalid_row(self):
        """Testa adição de linha com número inválido de colunas"""
        with self.assertRaises(ValueError):
            self.table.add_row([5, "Eve"])  # Faltando idade
    
    def test_get_row(self):
        """Testa a recuperação de linhas por índice"""
        row = self.table.get_row(0)
        self.assertEqual(row, [1, "Alice", 25])
    
    def test_get_invalid_row(self):
        """Testa recuperação com índice inválido"""
        with self.assertRaises(IndexError):
            self.table.get_row(10)  # Índice inexistente
    
    def test_remove_row(self):
        """Testa a remoção de linhas"""
        initial_row_count = len(self.table.rows)
        removed_row = self.table.remove_row(1)
        self.assertEqual(removed_row, [2, "Bob", 30])
        self.assertEqual(len(self.table.rows), initial_row_count - 1)
    
    def test_search(self):
        """Testa a função de busca na tabela"""
        results = self.table.search("Nome", "Alice")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], [1, "Alice", 25])
        
        # Testa busca por coluna inexistente
        with self.assertRaises(ValueError):
            self.table.search("Sobrenome", "Smith")
    
    def test_display(self):
        """Testa se o método display executa sem erros"""
        try:
            self.table.display()
            display_worked = True
        except:
            display_worked = False
        self.assertTrue(display_worked)

# Executa os testes no Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

Ran 13 tests in 0.011s

OK
| ID | Nome | Idade |
---------------------
| 1 | Alice | 25 |
| 2 | Bob | 30 |
| 3 | Charlie | 35 
