from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def open(self) -> None:
        self.browser.get(self.url)

    def wait_for_element(self, locator: tuple[By, str], timeout: int = 10):
        """
        Ожидает появления элемента на странице.
        :param locator: Локатор элемента, например (By.ID, 'id_value').
        :param timeout: Максимальное время ожидания (в секундах).
        :return: Найденный элемент.
        :raises TimeoutException: Если элемент не был найден за указанное время.
        """
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Элемент с локатором {locator} не найден на странице.")

    def click(self, locator: tuple[By, str]):
        """Клик на элемент"""
        try:
            element = self.wait_for_element(locator)
            element.click()
        except TimeoutException as e:
            raise TimeoutException(f"Не удалось нажать на элемент, ошибка {e}")

    def enter_text(self, locator: tuple[By, str], text: str):
        """Ввести текст в поле"""
        try:
            element = self.wait_for_element(locator)
            element.clear()
            element.send_keys(text)
        except TimeoutException as e:
            raise TimeoutException(f"Не удалось ввести текст в поле, ошибка {e}")

    def get_text(self, locator: tuple[By, str]) -> str:
        """Получить текст элемента"""
        try:
            element = self.wait_for_element(locator)
            return element.text
        except TimeoutException as e:
            raise TimeoutException(f"Не удалось получить текст из элемента, ошибка {e}")
