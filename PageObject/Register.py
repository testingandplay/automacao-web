# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from PageObject.FormPage import FormPage #page
from PageObject.data import User #dados de teste

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:/Users/silvi/Documentos/chromedriver.exe")
        self.driver.get("https://testingandplay.com/example/form")
        self.driver.implicitly_wait(2000)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_email_mandatory(self):
        form_page = FormPage(self.driver)
        form_page.set_email(User.email_empty)
        form_page.autocomplete_click()
        self.assertIn(User.email_mandatory, form_page.email_warning_check())

    def test_form_success(self):
        form_page = FormPage(self.driver)
        form_page.set_email(User.email_full)
        form_page.set_autocomplete(User.autocomplete)
        wait = WebDriverWait(self.driver, 20)
        form_page.wait_element(wait)
        form_page.city_click()
        select = form_page.get_select()
        all_options= form_page.get_alloption(select)
        form_page.selected_option_click(all_options,User.option3)
        form_page.set_text_area(User.textArea)
        form_page.set_file_input(User.file_input)
        form_page.set_password(User.password)
        form_page.radio2_click()
        form_page.check_click()
        form_page.image_click()
        #espera explicita
        form_page.poppup_click(wait)
        #assert no texto da popup
        self.assertIn(User.form_message, form_page.get_form_message())
        form_page.close_button_click()
        # fechar popup
        form_page.register_click()
        self.assertIn(User.success, form_page.toast_sucess_check())

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
