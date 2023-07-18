from selenium import webdriver

from Locators.order_data_scooter_page_locators import OrderDataScooterPageLocators
from Pages.order_data_scooter_page import OrderDataScooterPage
from Pages.order_data_user_page import OrderDataUserPage

options = webdriver.FirefoxOptions()
options.add_argument("--width=1920")
options.add_argument("--height=1020")


class TestOrderDataScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(options=options)

    def test_clik_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_user_page = OrderDataUserPage(self.driver)
        order_scooter_page = OrderDataScooterPage(self.driver)
        element = self.driver.find_element(*OrderDataScooterPageLocators.SCROLL_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*OrderDataScooterPageLocators.BUTTON_ORDER_MAIN).click()
        order_user_page.set_name('Маргарита')
        order_user_page.set_lastname('Авокадкина')
        order_user_page.set_adress('Балашиха, Тверская, 10')
        order_user_page.clik_metro()
        order_user_page.select_metro()
        order_user_page.set_number('89995554411')
        order_user_page.click_next()
        order_scooter_page.clik_delivery_time()
        order_scooter_page.select_data_delivery()
        order_scooter_page.click_rental_time()
        order_scooter_page.select_rental_time()
        order_scooter_page.select_color()
        order_scooter_page.set_comment('Доставьте быстрее')
        order_scooter_page.clik_order()
        order_scooter_page.clik_yes_order()
        assert self.driver.find_element(*OrderDataScooterPageLocators.TEXT_ORDER), "Тест не пройден"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
