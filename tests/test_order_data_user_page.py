from selenium import webdriver
from Locators.order_data_user_page_locators import OrderDataUserPageLocators
from Pages.order_data_user_page import OrderDataUserPage

options = webdriver.FirefoxOptions()
options.add_argument("--width=1920")
options.add_argument("--height=1020")


class TestOrderDataUser:
    driver = None

    def test_set_data_user_by_order(self, driver):
        order_user_page = OrderDataUserPage(driver)
        order_user_page.click_to_element(OrderDataUserPageLocators.BUTTON_ORDER)
        order_user_page.set_data_user_by_order()
        order_user_page.click_to_element(OrderDataUserPageLocators.BUTTON_NEXT)
        assert driver.find_element(*OrderDataUserPageLocators.TEXT_ORDER), "Тест не пройден"

