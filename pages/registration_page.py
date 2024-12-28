from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegistrationPage:
    URL = "https://demoqa.com/text-box"  # URL страницы регистрации

    # Локаторы
    FULL_NAME_INPUT = (By.CSS_SELECTOR, "#userName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.CSS_SELECTOR, "#permanentAddress")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    OUTPUT_NAME = (By.CSS_SELECTOR, "#name")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "#email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")
    OUTPUT_TEXT_BLOCK = (By.CSS_SELECTOR, "#output")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        """Открыть страницу формы."""
        self.driver.get(self.URL)

    def fill_form(self, full_name, email, current_address, permanent_address):
        """Заполнить форму."""
        self.driver.find_element(*self.FULL_NAME_INPUT).send_keys(full_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.CURRENT_ADDRESS_INPUT).send_keys(current_address)
        self.driver.find_element(*self.PERMANENT_ADDRESS_INPUT).send_keys(permanent_address)

    def submit_form(self):
        """Нажать кнопку Submit."""
        element = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)  # Прокрутка до элемента
        element.click()

    def get_output_text(self):
        """Получить текст из результатов после отправки формы."""
        return {
            "name": self.driver.find_element(*self.OUTPUT_NAME).text,
            "email": self.driver.find_element(*self.OUTPUT_EMAIL).text,
            "current_address": self.driver.find_element(*self.OUTPUT_CURRENT_ADDRESS).text,
            "permanent_address": self.driver.find_element(*self.OUTPUT_PERMANENT_ADDRESS).text,
        }

    def get_success_message(self):
        """Получает полный текст из блока после сабмита."""
        return self.driver.find_element(*self.OUTPUT_TEXT_BLOCK).text