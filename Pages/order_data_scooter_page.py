from Locators.order_data_scooter_page_locators import OrderDataScooterPageLocators


class OrderDataScooterPage:

    def __init__(self, driver):
        self.driver = driver

    def clik_delivery_time(self):
        self.driver.find_element(*OrderDataScooterPageLocators.DELIVERY_TIME_LOCATOR).click()

    def click_rental_time(self):
        self.driver.find_element(*OrderDataScooterPageLocators.RENTAL_TIME_LOCATOR).click()

    def select_data_delivery(self):
        self.driver.find_element(*OrderDataScooterPageLocators.DATA_DELIVERY).click()

    def select_rental_time(self):
        self.driver.find_element(*OrderDataScooterPageLocators.RENTAL_TIME).click()

    def select_color(self):
        self.driver.find_element(*OrderDataScooterPageLocators.COLOR_BLACK_LOCATOR).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderDataScooterPageLocators.COMMENT_LOCATOR).send_keys(comment)

    def clik_order(self):
        self.driver.find_element(*OrderDataScooterPageLocators.BUTTON_ORDER).click()

    def clik_yes_order(self):
        self.driver.find_element(*OrderDataScooterPageLocators.YES_LOCATOR).click()

