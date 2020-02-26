# -*- coding: utf-8 -*-
import unittest
import sys
from imp import reload

reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.close()

    def test_form_success(self):
        self.driver.get("https://testingandplay.com/example/form")
        self.driver.implicitly_wait(2000)
        # espera implicita
        email = self.driver.find_element_by_xpath("//input[@placeholder='Email']")
        email.send_keys("test@test.com")
        autocomplete = self.driver.find_element_by_xpath("//input[@id='typeahead-basic']")
        autocomplete.send_keys("new y")
        #espera explicita
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ngb-typeahead-0-0']")))
        city = self.driver.find_element_by_xpath("//button[@id='ngb-typeahead-0-0']")
        city.click()
         # percorrer opcoes do select para selecionar a opcao 3
        select = self.driver.find_element_by_xpath("//select[@id='select-input']")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            if option.text == '3':
                option.click()
        textarea = self.driver.find_element_by_xpath("//textarea[@id='textarea-input']")
        textarea.send_keys("texto texto texto texto texto texto")
        # enviar arquivo para campo de upload
        file_input = self.driver.find_element_by_xpath("//input[@id='file-input']")
        #file_input.send_keys("C:/Users/licol/Pictures/Sketchpad.png")
        file_input.send_keys("C:/Users/silvi/OneDrive/Imagens/funciona_minha_maquina.PNG")
        password = self.driver.find_element_by_xpath("//input[@placeholder='Senha']")
        password.send_keys("1234")
        radio = self.driver.find_element_by_xpath("//input[@id='radios2-input']")
        radio.click()
        check = self.driver.find_element_by_xpath("//input[@id='check-input']")
        check.click()
        image = self.driver.find_element_by_xpath("//div[@class='form-bg']//a//img")
        image.click()
        #espera explicita
        popup = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Fechar')]")))
        #assert no texto da popup
        self.assertIn("Este é um formulário de exemplo utilizado nos nossos cursos de automação web",
        self.driver.find_element_by_xpath("//p[contains(text(),'Este é um formulário de exemplo utilizado nos noss')]").text)
        fechar_button = self.driver.find_element_by_xpath("//button[contains(text(),'Fechar')]")
        fechar_button.click()
        # fechar popup
        cadastrar = self.driver.find_element_by_xpath("//button[@id='submit-input']")
        cadastrar.click()
        #assert na mensagem tast de sucesso
        self.assertIn("Sucesso",self.driver.find_element_by_xpath("//ngb-alert[@class='alert alert-success alert-dismissible']").text)

    def test_email_mandatory(self):
        self.driver.get("https://testingandplay.com/example/form")
        self.driver.implicitly_wait(2000)
        email = self.driver.find_element_by_xpath("//input[@placeholder='Email']")
        email.send_keys("")
        autocomplete = self.driver.find_element_by_xpath("//input[@id='typeahead-basic']")
        autocomplete.click()
        self.assertIn("Email obrigatório",
                      self.driver.find_element_by_xpath("//div[@class='invalid-feedback']").text)

if __name__ == '__main__':
    unittest.main()
