import pytest
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("--width=1920")
options.add_argument("--height=1020")


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(options=options)
    driver.get('https://qa-scooter.praktikum-services.ru/')

    yield driver
    driver.quit()
