import pytest
from Locators.main_page_locators import MainPageLocators
from Pages.main_pages import QuestionsPage


class TestQuestion:
    driver = None

    @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_clik_question(self, driver, number):
        question_page = QuestionsPage(driver)
        question_page.scroll_to_element(MainPageLocators.SCROLL_LOCATOR)
        method, locator = MainPageLocators.QUESTION_LOCATOR
        locator = method, locator.format(number)
        question_page.wait_visibility(locator)
        question_page.click_to_element(locator)
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = method, locator.format(number)
        question_page.wait_visibility(locator)
        question_page.check_clik_question(number)

    def test_clik_to_yandex(self, driver):
        question_page = QuestionsPage(driver)
        question_page.click_to_element(MainPageLocators.BUTTON_YANDEX)
        question_page.switch_to_window()
        question_page.wait_visibility(MainPageLocators.TEXT_ON_YANDEX)
        assert driver.find_element(*MainPageLocators.TEXT_ON_YANDEX), "Тест не пройден"

    def test_clik_to_scooter(self, driver):
        question_page = QuestionsPage(driver)
        question_page.click_to_element(MainPageLocators.BUTTON_ORDER)
        question_page.click_to_element(MainPageLocators.BUTTON_SCOOTER)
        assert driver.find_element(*MainPageLocators.TEXT_ON_MAIN), "Тест не пройден"
