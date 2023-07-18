import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Locators.main_page_locators import MainPageLocators
from Pages.main_pages import QuestionsPage

options = webdriver.FirefoxOptions()
options.add_argument("--width=1920")
options.add_argument("--height=1020")


class TestQuestion:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(options=options)

    @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_clik_question(self, number):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        question_page = QuestionsPage(self.driver)
        question_page.clik_question(number)
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = method, locator.format(number)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        question_page.check_clik_question(number)

    def test_clik_to_yandex(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        question_page = QuestionsPage(self.driver)
        question_page.clik_to_yandex()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.TEXT_ON_YANDEX))
        assert '/dzen.ru' in self.driver.current_url, "Тест не пройден"

    def test_clik_to_scooter(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        question_page = QuestionsPage(self.driver)
        question_page.clik_to_order()
        question_page.clik_to_scooter()
        assert self.driver.find_element(*MainPageLocators.TEXT_ON_MAIN), "Тест не пройден"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
