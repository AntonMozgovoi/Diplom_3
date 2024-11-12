from selenium.webdriver.common.by import By

class MainPageLocators:
    ENTER_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]')
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

    ORDER_IN_HISTORY = (By.XPATH, '//*[@class="OrderFeed_list__OLh59"]/child::*[1]')
    MODAL_WINDOW = (By.XPATH, '//*[contains(@Class, "Modal_orderBox")]')
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    WINDOW_SUCCESS_ORDER = (By.XPATH, '//*[contains(@class,"Modal_modal__contentBox")]')
    NUMBER_OF_ORDER = (By.XPATH, '//*[contains(@class,"Modal_modal__title_shadow")]')
    CLOSE_ORDER_WINDOW = (By.XPATH, '//button[contains(@Class,"Modal_modal__close_modified")]')
    NUMBER_ORDER_IN_HISTORY = (By.XPATH, '//*[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]/child::*[last()]/descendant::*[@class="text text_type_digits-default"]')
    COUNTER_FOR_ALL_TIME = (By.XPATH, '//*[contains(@Class,"OrderFeed_number")]')
    COUNTER_ORDER_TODAY = (By.XPATH, '//*[contains(@Class, "text text_type_main-medium") and text()="Выполнено за сегодня:"]/following-sibling::*[contains(@Class,"OrderFeed_number")]')
    NUMBER_OF_ORDER_IN_WORK = (By.XPATH, '//*[@class="text text_type_digits-default mb-2"]/ancestor::*[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]')

class ConstructorLocators:
    LIST_ORDER = By.XPATH, '//*[@Class="text text_type_digits-default"]'
    CROSS = (By.XPATH, '//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/descendant::button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    INGREDIENT = (By.XPATH, '//img[@alt="Соус фирменный Space Sauce"]')
    CONSTRUCTOR = (By.XPATH, '//*[text()="Перетяните булочку сюда (верх)"]')
    COUNTER = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient") and (@href="/ingredient/61c0c5a71d1f82001bdaaa73")]/descendant::*[contains(@class,"counter_counter__num")]')
    BUNS = (By.XPATH,'//*[@class="counter_counter__ZNLkj counter_default__28sqi"]/ancestor::*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')
    FIND_NUMBER_OF_ORDER = (By.XPATH, '//*[contains(text(),"151")]')