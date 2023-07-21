from Locators.main_page_locators import MainPageLocators
from Pages.base_page import BasePage
from data import TestData


class QuestionsPage(BasePage):

    def check_clik_question(self, number):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = locator.format(number)
        actually_value = self.driver.find_element(method, locator).text
        expected_value = TestData.ANSWER_LIST[number]
        assert actually_value == expected_value, f'Ожидалось значение поля: "{expected_value}", получено "{actually_value}"'
