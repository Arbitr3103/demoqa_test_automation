from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage  # Явный импорт


class CheckBoxPage(BasePage):
    URL = "https://demoqa.com/checkbox"

    # Локаторы
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Collapse all']")
    HOME_CHECKBOX = (By.CSS_SELECTOR, "label[for='tree-node-home'] span.rct-checkbox")
    RESULTS_TEXT = (By.CSS_SELECTOR, "#result")

    def __init__(self, browser: WebDriver):
        super().__init__(browser, self.URL)  # Вызываем конструктор родителя

    def open(self) -> None:  # Добавили подсказку типов
        """Открыть страницу"""
        super().open()  # Убрали self.url

    def expand_all_checkboxes(self):
        """Раскрыть все чекбоксы"""
        expand_button = self.wait_for_element(self.EXPAND_ALL_BUTTON)  # Добавили self.
        expand_button.click()

    def collapse_all_checkboxes(self):
        """Свернуть все чекбоксы"""
        collapse_button = self.wait_for_element(self.COLLAPSE_ALL_BUTTON)  # Добавили self.
        collapse_button.click()

    def select_home_checkbox(self):
        """Поставить галочку в чекбоксе 'Home'."""
        home_checkbox = self.wait_for_element(self.HOME_CHECKBOX)  # Добавили self.
        home_checkbox.click()

    def get_results_text(self) -> str:  # Добавили подсказку типов
        """Получить текст из блока с результатами."""
        return self.wait_for_element(self.RESULTS_TEXT).text  # Добавили self.
