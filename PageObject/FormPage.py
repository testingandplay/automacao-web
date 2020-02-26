from PageObject.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FormPage(BasePage):
    email = "//input[@placeholder='Email']"
    autocomplete = "//input[@id='typeahead-basic']"
    element = "//button[@id='ngb-typeahead-0-0']"
    city = "//button[@id='ngb-typeahead-0-0']"
    select = "//select[@id='select-input']"
    all_options = "option"
    textarea = "//textarea[@id='textarea-input']"
    file_input = "//input[@id='file-input']"
    password = "//input[@placeholder='Senha']"
    radio2 = "//input[@id='radios2-input']"
    check = "//input[@id='check-input']"
    image = "//div[@class='form-bg']//a//img"
    popup = "//button[contains(text(),'Fechar')]"
    toast_sucess= "//ngb-alert[@class='alert alert-success alert-dismissible']"
    email_warning= "//div[@class='invalid-feedback']"
    register_button = "//button[@id='submit-input']"
    form_message = "//p[contains(text(),'Este é um formulário de exemplo utilizado nos noss')]"
    close_button = "//button[contains(text(),'Fechar')]"

    def set_email(self, email):
        self._driver.find_element_by_xpath(FormPage.email).send_keys(email)

    def set_autocomplete(self, autocomplete):
        self._driver.find_element_by_xpath(FormPage.autocomplete).send_keys(autocomplete)

    def autocomplete_click(self):
        self._driver.find_element_by_xpath(FormPage.autocomplete).click()

    def set_text_area(self, textarea):
        self._driver.find_element_by_xpath(FormPage.textarea).send_keys(textarea)

    def set_password(self, password):
        self._driver.find_element_by_xpath(FormPage.password).send_keys(password)

    def set_file_input(self, file):
        self._driver.find_element_by_xpath(FormPage.file_input).send_keys(file)

    def get_select(self):
        select = self._driver.find_element_by_xpath(FormPage.select)
        return select

    def get_alloption(self, select):
        all_options = select.find_elements_by_tag_name(FormPage.all_options)
        return all_options

    def selected_option_click(self, all_options, selected_option):
        for option in all_options:
            if option.text == selected_option:
                option.click()

    def wait_element(self, wait):
       element = wait.until(EC.element_to_be_clickable((By.XPATH, FormPage.element)))

    def city_click(self):
        self._driver.find_element_by_xpath(FormPage.city).click()

    def radio2_click(self):
        radio = self._driver.find_element_by_xpath(FormPage.radio2).click()

    def check_click(self):
        check = self._driver.find_element_by_xpath(FormPage.check).click()

    def image_click(self):
        radio = self._driver.find_element_by_xpath(FormPage.image).click()

    def register_button_click(self):
        self._driver.find_element_by_xpath(FormPage.register_button).click()

    def poppup_click(self, wait):
        popup = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Fechar')]")))
        popup.click()

    def close_button_click(self):
        close_button = self._driver.find_element_by_xpath(FormPage.close_button)
        close_button.click()

    def get_form_message(self):
        form_message = self._driver.find_element_by_xpath(FormPage.form_message)
        return form_message.text

    def toast_sucess_check(self):
        return self._driver.find_element_by_xpath(FormPage.toast_sucess).text

    def email_warning_check(self):
        return self._driver.find_element_by_xpath(FormPage.email_warning).text
