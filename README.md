# Aula-prof-rodrigo
Atividade-Avaliativa-QA
📄 Estrutura do README.md (Obrigatória)
1. Apresentação
Nome completo
Renato Francelino Da Silva

Curso e semestre
GTI 5NA 5- SEMESTRE 

Um parágrafo com uma breve descrição da sua experiência com a disciplina
Muito boa a disciplina, gostando muito do apeendizado!

2. O que é Quality Assurance (QA)?
Explique com suas palavras o conceito de QA e sua importância no desenvolvimento de software
Uma garantia de qualidade, onde através de ferramentas sao feitos testes, para empresas efetuarem suas atividades com acertividade.

Use uma linguagem simples e acessível, como se estivesse explicando para alguém leigo
Um Perito em qaulidade acertiva



3. Conceitos Aprendidos Durante o Semestre
Escreva um parágrafo explicando o que você aprendeu sobre:
Qualidade em software e cultura de qualidade
Testam o aplicativo em diferentes dispositivos para garantir que funcione bem em todos.

Tipos de testes (unitário, integração, sistema, aceitação, regressão e exploratório)


Planejamento de testes (critérios de aceitação, planos e casos de teste)


Ferramentas de testes utilizadas durante o semestre (Colab, GitHub, etc.)


Automação de testes e integração com CI/CD


Monitoramento e controle de qualidade (uso de métricas, rastreamento de bugs, observabilidade)


4. Ferramentas e Sites Utilizados
Liste todos os sites e ferramentas que você usou durante o curso, por exemplo:

https://reqres.in/
sim 

https://colab.research.google.com/ 
sim

https://github.com/
sim

https://uptimerobot.com/
sim

(outros que desejar incluir)


5. Explicação dos Testes Entregues
Para cada um dos três testes obrigatórios entregues na pasta /testes, responda:
Nome do teste


Objetivo


Qual biblioteca Python foi utilizada
Google Colab

Qual resultado esperado
100%

Link para o arquivo (ex: testes/teste_01.py)
https://colab.research.google.com/drive/1u4nEp5hNE0ZixcMSjN9BpzPk4cCaSjQW?usp=sharing
teste_01 class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()
    
    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)
        self.assertEqual(self.calc.somar(-1, 1), 0)
        self.assertEqual(self.calc.somar(0, 0), 0)
    
    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(5, 3), 2)
        self.assertEqual(self.calc.subtrair(-1, -1), 0)
        self.assertEqual(self.calc.subtrair(0, 0), 0)
    
    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-1, 5), -5)
        self.assertEqual(self.calc.multiplicar(0, 10), 0)
    
    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(9, 3), 3)
        self.assertAlmostEqual(self.calc.dividir(1, 3), 0.333333, places=6)
        
    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


teste_02  Tabela:
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

teste_03  Saucedemo(site aleatorío)(Aceitação) 

!pip install selenium webdriver-manager pytest allure-pytest
!apt-get update
!apt install -y chromium-chromedriver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    """Configura o navegador para os testes"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def setup(browser):
    """Prepara o ambiente para cada teste"""
    browser.get("https://www.saucedemo.com/")
    yield
    # Limpeza após cada teste (opcional)
    browser.delete_all_cookies()

@pytest.mark.acceptance
def test_login_com_sucesso(browser, setup):
    """CT-001: Login com credenciais válidas"""
    # Preenche formulário de login
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # Verifica se foi redirecionado para a página de produtos
    assert "inventory.html" in browser.current_url
    assert browser.find_element(By.CLASS_NAME, "title").text == "PRODUCTS"

@pytest.mark.acceptance
def test_adicionar_produto_ao_carrinho(browser, setup):
    """CT-002: Adicionar produto ao carrinho"""
    # Realiza login
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # Adiciona produto ao carrinho
    product_name = "Sauce Labs Backpack"
    browser.find_element(By.XPATH, f"//div[text()='{product_name}']/../../..//button").click()
    
    # Verifica se o ícone do carrinho foi atualizado
    cart_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"
    
    # Acessa o carrinho e verifica o produto
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert browser.find_element(By.CLASS_NAME, "inventory_item_name").text == product_name

@pytest.mark.acceptance
def test_finalizar_compra_com_sucesso(browser, setup):
    """CT-003: Fluxo completo de compra"""
    # Realiza login
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # Adiciona produto ao carrinho
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    # Acessa o carrinho
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Inicia checkout
    browser.find_element(By.ID, "checkout").click()
    
    # Preenche informações
    browser.find_element(By.ID, "first-name").send_keys("Fulano")
    browser.find_element(By.ID, "last-name").send_keys("de Tal")
    browser.find_element(By.ID, "postal-code").send_keys("12345678")
    browser.find_element(By.ID, "continue").click()
    
    # Finaliza compra
    browser.find_element(By.ID, "finish").click()
    
    # Verifica mensagem de sucesso
    assert browser.find_element(By.CLASS_NAME, "complete-header").text == "THANK YOU FOR YOUR ORDER"
    assert browser.find_element(By.CLASS_NAME, "complete-text").text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

@pytest.mark.acceptance
def test_login_com_credenciais_invalidas(browser, setup):
    """CT-004: Login com credenciais inválidas"""
    # Preenche formulário com credenciais inválidas
    browser.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    browser.find_element(By.ID, "password").send_keys("senha_errada")
    browser.find_element(By.ID, "login-button").click()
    
    # Verifica mensagem de erro
    error_message = browser.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Epic sadface: Username and password do not match any user in this service" in error_message.text

# Executa os testes com relatório Allure
if __name__ == "__main__":
    import os
    pytest.main(["-v", "-m", "acceptance", "--alluredir=allure-results"])
    os.system("allure serve allure-results")

============================= test session starts ==============================
platform linux -- Python 3.11.12, pytest-8.3.5, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /content
plugins: allure-pytest-2.14.2, langsmith-0.3.42, anyio-4.9.0, typeguard-4.4.2
collecting ... collected 0 items

============================ no tests ran in 0.04s =============================
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


Ran 13 tests in 0.011s

OK
| ID | Nome | Idade |
---------------------
| 1 | Alice | 25 |
| 2 | Bob | 30 |
| 3 | Charlie | 35 
# Para executar os testes no Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



Ran 5 tests in 0.011s
Exemplo de formatação:

✅ Teste 01 – Verificação de status da API ReqRes
Biblioteca: Requests


Objetivo: Verificar se o endpoint retorna status HTTP 200


Resultado esperado: Teste passa com sucesso se o status for 200


Arquivo: testes/teste_01.py/teste_02.py/teste_03.py
https://colab.research.google.com/drive/1u4nEp5hNE0ZixcMSjN9BpzPk4cCaSjQW?usp=sharing


6. Conclusão Final
Escreva um parágrafo com sua reflexão pessoal, respondendo:
O que você aprendeu de mais importante?
TUDO! Vi que o aprendizado de QA é muito importante para q uma(site ou empresa) funcione adequadamente.

Como você enxerga a área de QA no seu futuro profissional?
Pretendo me especializar ainda mais na área para seguir carreira.

Qual ferramenta ou tema mais chamou sua atenção e por quê?
COLAB! Pela facilidade da ferramenta e sempre proporcionar correção em caso de código incorreto


🐍 Requisitos dos Testes Python
Você deve entregar no mínimo três testes desenvolvidos em Python, com as seguintes características:
Estar dentro da pasta /testes


Ter sido feito com base nas atividades vistas em aula


Utilizar bibliotecas como requests, unittest, pytest, entre outras básicas


Estar comentado e com lógica compreensível
