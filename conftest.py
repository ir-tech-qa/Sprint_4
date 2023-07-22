import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1020")
    driver = webdriver.Firefox(options=options)
    driver.get('https://qa-scooter.praktikum-services.ru/')

    yield driver
    driver.quit()
