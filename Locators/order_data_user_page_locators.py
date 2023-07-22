from selenium.webdriver.common.by import By

class OrderDataUserPageLocators:
    NAME_LOCATOR = By.XPATH, './/*[@placeholder= "* Имя"]' #
    LASTNAME_LOCATOR = By.XPATH, './/*[@placeholder= "* Фамилия"]' #
    ADRESS_LOCATOR = By.XPATH, './/*[@placeholder= "* Адрес: куда привезти заказ"]'
    METRO_LOCATOR = By.XPATH, './/*[@placeholder= "* Станция метро"]'
    NUMBER_LOCATOR = By.XPATH, './/*[@placeholder= "* Телефон: на него позвонит курьер"]'
    BUTTON_ORDER = By.XPATH, './/button[@class = "Button_Button__ra12g"]'
    BUTTON_NEXT = By.XPATH, './/button[text() = "Далее"]'  #
    METRO_STATION = By.XPATH, './/*[@data-value = "3"]'
    TEXT_ORDER = By.XPATH, './/*[text() = "Про аренду"]'
