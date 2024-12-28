import pytest
from pages.radio_button_page import RadioButtonPage


@pytest.mark.radio
def test_radio_buttons(browser):
    """
    Тест на проверку функциональности радио-кнопок.
    """
    radio_buttons_page = RadioButtonPage(browser)

    # Шаг 1: Открыть страницу с радио-кнопками
    radio_buttons_page.open()

    # Шаг 2: Проверить радио-кнопки "Yes" и "Impressive"
    radio_buttons_page.select_radio_buttons("Yes")
    assert radio_buttons_page.get_selected_message() == "You have selected Yes", "Сообщение не 'Yes'!"

    radio_buttons_page.select_radio_buttons("Impressive")
    assert radio_buttons_page.get_selected_message() == "You have selected Impressive", "Сообщение не  'Impressive'!"

    # Шаг 3: Проверить, что кнопка "No" недоступна
    assert radio_buttons_page.is_radio_button_disabled("No"), "Кнопка 'No' доступна для выбора, что некорректно!"
