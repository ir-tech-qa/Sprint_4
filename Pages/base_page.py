from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        scroll_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_visibility(self,locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def set_text_on_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
