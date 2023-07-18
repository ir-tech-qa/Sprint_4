from selenium.webdriver.common.by import By


class OrderDataScooterPageLocators:
    DELIVERY_TIME_LOCATOR = By.XPATH, './/*[@placeholder= "* Когда привезти самокат"]'  #
    RENTAL_TIME_LOCATOR = By.XPATH, './/*[text()= "* Срок аренды"]'  #
    ADRESS_LOCATOR = By.XPATH, './/*[@placeholder= "* Адрес: куда привезти заказ"]'
    COLOR_BLACK_LOCATOR = By.XPATH, './/*[@id="black"]'
    COMMENT_LOCATOR = By.XPATH, './/*[@placeholder= "Комментарий для курьера"]'
    BUTTON_ORDER_MAIN = By.XPATH, './/button[@class = "Button_Button__ra12g Button_UltraBig__UU3Lp"]'
    BUTTON_ORDER = By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]'
    DATA_DELIVERY = By.XPATH, '//*[@aria-label="Choose воскресенье, 30-е июля 2023 г."]'  #
    RENTAL_TIME = By.XPATH, './/*[text() = "двое суток"]'
    YES_LOCATOR = By.XPATH, '.// button[text() = "Да"]'
    TEXT_ORDER = By.XPATH, './/*[text()= "Заказ оформлен"]'
    SCROLL_LOCATOR =  By.XPATH, './/*[text()= "Как это работает"]'


