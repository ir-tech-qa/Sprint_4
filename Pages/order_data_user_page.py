from Locators.order_data_user_page_locators import OrderDataUserPageLocators
from Pages.base_page import BasePage


class OrderDataUserPage(BasePage):

    def set_data_user_by_order(self):
        self.set_text_on_field(OrderDataUserPageLocators.NAME_LOCATOR, 'Светлана')
        self.set_text_on_field(OrderDataUserPageLocators.LASTNAME_LOCATOR, 'Золотова')
        self.set_text_on_field(OrderDataUserPageLocators.ADRESS_LOCATOR, 'Москва, Красный бульвар, 5')
        self.click_to_element(OrderDataUserPageLocators.METRO_LOCATOR)
        self.click_to_element(OrderDataUserPageLocators.METRO_STATION)
        self.set_text_on_field(OrderDataUserPageLocators.NUMBER_LOCATOR, '89995554433')

