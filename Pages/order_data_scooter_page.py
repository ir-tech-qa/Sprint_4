from Locators.order_data_scooter_page_locators import OrderDataScooterPageLocators
from Pages.base_page import BasePage


class OrderDataScooterPage(BasePage):
    def set_data_scooter_by_order(self):
        self.click_to_element(OrderDataScooterPageLocators.DELIVERY_TIME_LOCATOR)
        self.click_to_element(OrderDataScooterPageLocators.DATA_DELIVERY)
        self.click_to_element(OrderDataScooterPageLocators.RENTAL_TIME_LOCATOR)
        self.click_to_element(OrderDataScooterPageLocators.RENTAL_TIME)
        self.click_to_element(OrderDataScooterPageLocators.COLOR_BLACK_LOCATOR)
        self.set_text_on_field(OrderDataScooterPageLocators.COMMENT_LOCATOR, 'Доставьте быстрее')


