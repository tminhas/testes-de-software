import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class DuckDuckGoCalculatorTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://duckduckgo.com/")
        self.wait = WebDriverWait(self.driver, 20)  # Aumentei o tempo de espera para 20 segundos

    def tearDown(self):
        self.driver.quit()

    def realizar_operacao(self, operacao, resultado_esperado):
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.clear()
        search_box.send_keys(operacao + Keys.RETURN)
        
        resultado = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="display"]'))
        )
        self.assertEqual(resultado.text, resultado_esperado)

    def test_somar_dois_numeros(self):
        self.realizar_operacao("2 + 3", "5")

    def test_somar_e_dividir(self):
        self.realizar_operacao("(2 + 3) / 10", "0.5")

    def test_duas_operacoes(self):
        self.realizar_operacao("3 + 3", "6")
        self.realizar_operacao("5 * 2", "10")

    def test_tres_operacoes_no_historico(self):
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.clear()
        search_box.send_keys('2 - 2')
        search_box.send_keys(Keys.RETURN)
        calc_display = self.driver.find_element(By.CSS_SELECTOR, '#clear_button')
        calc_display.send_keys('2*3')
        BotaoIgual = self.driver.find_element(By.CSS_SELECTOR,
                                              '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(18)')
        BotaoIgual.click()
        calc_display.send_keys('8/2')
        BotaoIgual = self.driver.find_element(By.CSS_SELECTOR,
                                              '#zci-calculator > div > div > div > div > div > div.tile__tabs > div.tile__calc__col.tile__tab__basic > button:nth-child(18)')
        BotaoIgual.click()
        hist_1 = self.driver.find_element(By.CSS_SELECTOR,'#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(1) > span.tile__past-result.one-line').text
        hist_2 = self.driver.find_element(By.CSS_SELECTOR,'#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(2) > span.tile__past-result.one-line').text
        hist_3 = self.driver.find_element(By.CSS_SELECTOR,'#zci-calculator > div > div > div > div > div > div.tile__tabs > ul > li:nth-child(3) > span.tile__past-result.one-line').text

        self.assertEqual(hist_3, '0', f"Resultado esperado '0', mas obteve '{hist_3}'")
        self.assertEqual(hist_2, '6', f"Resultado esperado '6', mas obteve '{hist_2}'")
        self.assertEqual(hist_1, '4', f"Resultado esperado '4', mas obteve '{hist_1}'")



if __name__ == "__main__":
    unittest.main()