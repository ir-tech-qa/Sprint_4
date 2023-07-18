from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, './/*[@id = "accordion__heading-{}"]' # локаторы вопросов
    ANSWER_LOCATOR = By.XPATH, '.// *[@id = "accordion__panel-{}"]/p'# локаторы ответов на вопросы
    SCROLL_LOCATOR = By.XPATH, './/*[text() = "Вопросы о важном"]'# текст для прокрутки вниз
    BUTTON_ORDER = By.XPATH, './/button[@class = "Button_Button__ra12g"]'# кнопка заказа
    BUTTON_SCOOTER = By.XPATH, './/img[@alt = "Scooter"]' # кнопка для перехода на главную страницу "Самокат"
    BUTTON_YANDEX = By.XPATH, './/img[@alt = "Yandex"]' # кнопка для перехода на страницу Яндекса
    TEXT_ON_MAIN = By.XPATH, './/*[text() = "Самокат "]' #текст заголовка на главной странице
    TEXT_ON_YANDEX = By.XPATH, '.// button[text() = "Найти"]'

