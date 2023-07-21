from selenium import webdriver

from Locators.order_data_scooter_page_locators import OrderDataScooterPageLocators
from Locators.order_data_user_page_locators import OrderDataUserPageLocators
from Pages.order_data_scooter_page import OrderDataScooterPage

options = webdriver.FirefoxOptions()
options.add_argument("--width=1920")
options.add_argument("--height=1020")


class TestOrderDataScooter:
    driver = None

    def test_clik_order(self, driver):
        order_scooter_page = OrderDataScooterPage(driver)
        order_scooter_page.scroll_to_element(OrderDataScooterPageLocators.SCROLL_LOCATOR)
        order_scooter_page.click_to_element(OrderDataScooterPageLocators.BUTTON_ORDER_MAIN)
        order_scooter_page.set_text_on_field(OrderDataUserPageLocators.NAME_LOCATOR, 'Светлана')
        order_scooter_page.set_text_on_field(OrderDataUserPageLocators.LASTNAME_LOCATOR, 'Золотова')
        order_scooter_page.set_text_on_field(OrderDataUserPageLocators.ADRESS_LOCATOR, 'Москва, Красный бульвар, 5')
        order_scooter_page.click_to_element(OrderDataUserPageLocators.METRO_LOCATOR)
        order_scooter_page.click_to_element(OrderDataUserPageLocators.METRO_STATION)
        order_scooter_page.set_text_on_field(OrderDataUserPageLocators.NUMBER_LOCATOR, '89995554433')
        order_scooter_page.click_to_element(OrderDataUserPageLocators.BUTTON_NEXT)
        order_scooter_page.set_data_scooter_by_order()
        order_scooter_page.click_to_element(OrderDataScooterPageLocators.BUTTON_ORDER)
        order_scooter_page.click_to_element(OrderDataScooterPageLocators.YES_LOCATOR)
        assert driver.find_element(*OrderDataScooterPageLocators.TEXT_ORDER), "Тест не пройден"
