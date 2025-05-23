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
