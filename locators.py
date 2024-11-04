from selenium.webdriver.common.by import By

class MainPageLocators:
    ENTER_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]') # кнопка "Войти в аккаунт"
    ENTER_RECOVERY_PASSWORD = (By.XPATH, '//*[contains(@Class, "Auth_link") and text()="Восстановить пароль"]')
    FIELD_INPUT_EMAIL = (By.XPATH, '//input[@Class="text input__textfield text_type_main-default"]')
    BUTTON_RECOVER = (By.XPATH, '//button[contains(@Class, "button_button_size_medium") and text()="Восстановить"]')
    FIELD_NEW_PASSWORD = (By.XPATH, '//*[@name="Введите новый пароль"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@Class ="input__icon input__icon-action"]')
    PERSONAL_ACCOUNT = (By.XPATH, '//*[contains(@Class, "AppHeader_header__linkText") and text()="Личный Кабинет"]')
    FIELD_AUTH_EMAIL = (By.XPATH, '//*[@name="name"]')
    PASSWORD_AUTH_PASS = (By.XPATH, '//*[@name="Пароль"]')
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')
    HISTORY_ORDER_LINK = (By.XPATH, '//*[text()="История заказов"]')
    LOGOUT_LINK = (By.XPATH, '//*[text()="Выход"]')
    INPUT_PASSWORD_FIELD = (By.NAME, "Пароль")

class Header:
    CONSTRUCTOR = (By.XPATH, '//*[text()="Конструктор"]')
    ORDER_LIST = (By.XPATH, '//*[text()="Лента Заказов"]')

class OrderFeed:
    ORDER_IN_HISTORY = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a')
    MODAL_WINDOW = (By.XPATH, '//*[contains(@Class, "Modal_orderBox")]')
    CROSS = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/button')
    INGREDIENT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[2]/img')
    CONSTRUCTOR = (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div/span/span[1]')
    COUNTER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[2]/div[1]/p')
    BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]/img')
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    WINDOW_SUCCESS_ORDER = (By.XPATH, '//*[@id="root"]/div/section/div[1]/div')
    ORDER_FROM_FEED = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]')
    NUMBER_OF_ORDER = (By.XPATH, '//*[@id ="root"]/div/section/div[1]/div/h2')
    CLOSE_ORDER_WINDOW = (By.XPATH, '//*[@id="root"]/div/section/div[1]/button')
    NUMBER_ORDER_IN_FEED = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[2]/a/div[1]/p[1]')
    NUMBER_ORDER_IN_HISTORY = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[last()]/a/div[1]/p[1]')
    COUNTER_FOR_ALL_TIME = (By.XPATH, '//*[contains(@Class,"OrderFeed_number")]')
    COUNTER_ORDER_TODAY = (By.XPATH, '//*[@id ="root"]/div/main/div/div/div/div[3]/p[2]')
    NUMBER_OF_ORDER_IN_WORK = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li')

class ConstructorLocators:
    LIST_ORDER = (By.XPATH, '//*[@Class="text text_type_digits-default"]')