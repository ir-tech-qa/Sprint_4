from selenium.webdriver.common.by import By


class OrderDataScooterPageLocators:
    DELIVERY_TIME_LOCATOR = By.XPATH, './/*[@placeholder= "* Когда привезти самокат"]'  #
    RENTAL_TIME_LOCATOR = By.XPATH, './/*[text()= "* Срок аренды"]'  #
    ADRESS_LOCATOR = By.XPATH, './/*[@placeholder= "* Адрес: куда привезти заказ"]'
    COLOR_BLACK_LOCATOR = By.XPATH, './/*[@id="black"]'
    COMMENT_LOCATOR = By.XPATH, './/*[@placeholder= "Комментарий для курьера"]'
    BUTTON_ORDER_MAIN = By.XPATH, './/div[contains(@class , "Home_FinishButton")]/button[contains(text(), "Заказать")]'
    BUTTON_ORDER = By.XPATH, './/div[contains(@class , "Order_Buttons")]/button[contains(text(), "Заказать")]'
    DATA_DELIVERY = By.XPATH, './/*[@class="react-datepicker__day react-datepicker__day--028"]'  #
    RENTAL_TIME = By.XPATH, './/*[text() = "двое суток"]'
    YES_LOCATOR = By.XPATH, '.// button[text() = "Да"]'
    TEXT_ORDER = By.XPATH, './/*[text()= "Заказ оформлен"]'
    SCROLL_LOCATOR =  By.XPATH, './/*[text()= "Как это работает"]'


