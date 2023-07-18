from selenium import webdriver
from Locators.order_data_user_page_locators import OrderDataUserPageLocators
from Pages.order_data_user_page import OrderDataUserPage

options = webdriver.FirefoxOptions()
options.add_argument("--width=1920")
options.add_argument("--height=1020")


class TestOrderDataUser:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(options=options)

    def test_clik_next(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_user_page = OrderDataUserPage(self.driver)
        self.driver.find_element(*OrderDataUserPageLocators.BUTTON_ORDER).click()
        order_user_page.set_name('Светлана')
        order_user_page.set_lastname('Золотова')
        order_user_page.set_adress('Москва, Красный бульвар, 5')
        order_user_page.clik_metro()
        order_user_page.select_metro()
        order_user_page.set_number('89995554433')
        order_user_page.click_next()
        assert self.driver.find_element(*OrderDataUserPageLocators.TEXT_ORDER), "Тест не пройден"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
