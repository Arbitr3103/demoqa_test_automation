from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButtonPage:
    URL = "https://demoqa.com/radio-button"

    # Локаторы для радио-кнопок и сообщения
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, "label[for='yesRadio']")
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, "label[for='noRadio']")
    SELECTED_MESSAGE = (By.CSS_SELECTOR, ".mt-3")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        """Открыть страницу радио-кнопок."""
        self.driver.get(self.URL)

    def select_radio_buttons(self, option: str):
        """
        Выбрать радио-кнопку по имени.
        :param option: Название опции, которую нужно выбрать ('Yes', 'Impressive').
        """
        if option == "Yes":
            self.driver.find_element(*self.RADIO_BUTTON_YES).click()
        elif option == "Impressive":
            self.driver.find_element(*self.RADIO_BUTTON_IMPRESSIVE).click()
        elif option == "No":
            raise ValueError("Кнопка 'No' недоступна для выбора.")
        else:
            raise ValueError(f"Неизвестный вариант: {option}")

    def get_selected_message(self):
        """Получить сообщение, соответствующее выбранной кнопке."""
        return self.driver.find_element(*self.SELECTED_MESSAGE).text

    def is_radio_button_disabled(self, option: str):
        """Проверить, отключена ли радио-кнопка."""
        if option == "No":
            no_radio = self.driver.find_element(*self.RADIO_BUTTON_NO)
            return "disabled" in no_radio.get_attribute("class")
        raise ValueError(f"Проверка доступности невозможна для варианта: {option}")
