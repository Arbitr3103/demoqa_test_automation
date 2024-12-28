import pytest
import logging
from pages.checkbox_page import CheckBoxPage

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.checkbox
def test_check_all_checkboxes(browser):
    """
    Тест на проверку работы чекбоксов.

    Шаги:
    1. Открыть страницу чекбоксов.
    2. Раскрыть все чекбоксы.
    3. Выбрать чекбокс Home.
    4. Проверить наличие текста "You have selected :
    home
    desktop
    notes
    commands
    documents
    workspace
    react
    angular
    veu
    office
    public
    private
    classified
    general
    downloads
    wordFile
    excelFile"
    """
    logger.info("Шаг 1: Создание объекта страницы CheckBoxPage")
    checkbox_page = CheckBoxPage(browser)

    logger.info("Шаг 2: Открытие страницы чекбоксов")
    checkbox_page.open()

    logger.info("Шаг 3: Развернуть все чекбоксы")
    checkbox_page.expand_all_checkboxes()

    logger.info("Шаг 4: Поставить галочку в чекбоксе Home")
    checkbox_page.select_home_checkbox()

    expected_text = "You have selected :\nhome\ndesktop\nnotes\ncommands\ndocuments\nworkspace\nreact\nangular\nveu\noffice\npublic\nprivate\nclassified\ngeneral\ndownloads\nwordFile\nexcelFile"
    logger.info("Шаг 5: Получение текста")
    actual_text = checkbox_page.get_results_text()
    logger.info(f"Текст с сайта: {actual_text}")

    logger.info("Шаг 6: Проверка, что текст верный")
    assert actual_text == expected_text, f"Текст не соответствует ожидаемому!"
