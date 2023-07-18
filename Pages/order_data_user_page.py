from Locators.order_data_user_page_locators import OrderDataUserPageLocators


class OrderDataUserPage:

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*OrderDataUserPageLocators.NAME_LOCATOR).send_keys(name)

    def set_lastname(self, lastname):
        self.driver.find_element(*OrderDataUserPageLocators.LASTNAME_LOCATOR).send_keys(lastname)

    def set_adress(self, adress):
        self.driver.find_element(*OrderDataUserPageLocators.ADRESS_LOCATOR).send_keys(adress)

    def set_number(self, number):
        self.driver.find_element(*OrderDataUserPageLocators.NUMBER_LOCATOR).send_keys(number)

    def clik_metro(self):
        self.driver.find_element(*OrderDataUserPageLocators.METRO_LOCATOR).click()

    def select_metro(self):
        self.driver.find_element(*OrderDataUserPageLocators.METRO_STATION).click()

    def click_next(self):
        self.driver.find_element(*OrderDataUserPageLocators.BUTTON_NEXT).click()

