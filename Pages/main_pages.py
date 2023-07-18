from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Locators.main_page_locators import MainPageLocators
from data import TestData


class QuestionsPage:

    def __init__(self, driver):
        self.driver = driver

    def clik_question(self, number):
        element = self.driver.find_element(*MainPageLocators.SCROLL_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        method, locator = MainPageLocators.QUESTION_LOCATOR
        locator = method, locator.format(number)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def clik_to_scooter(self):
        self.driver.find_element(*MainPageLocators.BUTTON_SCOOTER).click()

    def clik_to_yandex(self):
        self.driver.find_element(*MainPageLocators.BUTTON_YANDEX).click()

    def clik_to_order(self):
        self.driver.find_element(*MainPageLocators.BUTTON_ORDER).click()

    def check_clik_question(self, number):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = locator.format(number)
        actually_value = self.driver.find_element(method, locator).text
        expected_value = TestData.ANSWER_LIST[number]
        assert actually_value == expected_value, f'Ожидалось значение поля: "{expected_value}", получено "{actually_value}"'
