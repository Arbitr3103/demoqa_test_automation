import pytest
import logging
from pages.registration_page import RegistrationPage

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.registration
def test_successful_registration(browser):
    registration_page = RegistrationPage(browser)

    # Шаги теста
    logger.info("Шаг 1: Открытие страницы регистрации")
    registration_page.open()

    logger.info("Шаг 2: Заполнение формы регистрации")
    registration_page.fill_form(
        full_name="Test User",
        email="testuser@gmail.com",
        current_address="123 Test St",
        permanent_address="456 Main St"
    )
    logger.info("Шаг 3: Отправка формы регистрации")
    registration_page.submit_form()

    logger.info("Шаг 4: Получение текста подтверждения")
    success_message = registration_page.get_output_text()
    logger.info(f"Текст подтверждения: {success_message}")

    logger.info("Шаг 5: Проверка, что имя пользователя отображается в подтверждении")
    assert "Test User" in success_message['name'], "Имя пользователя не отображается в подтверждении!"
    logger.info("Шаг 6: Проверка, что email отображается в подтверждении")
    assert "testuser@gmail.com" in success_message['email'], "Email не отображается в подтверждении!"
