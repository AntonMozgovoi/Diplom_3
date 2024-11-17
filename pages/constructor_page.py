import allure
from data import TestData
from locators import ConstructorLocators
from pages.base_page import BasePage


class Constructor(BasePage):
    @allure.step("переход на страницу конструктор")
    def transition_to_constructor(self):
        const = self.wait_and_find_element(ConstructorLocators.CONSTRUCTOR_MAIN)
        const.click()

    @allure.step("переход на страницу заказов")
    def transition_to_order_list(self):
        order_list = self.wait_and_find_element(ConstructorLocators.ORDER_LIST)
        order_list.click()

    @allure.step("выбор заказа из ленты заказов")
    def select_order_from_feed(self):
        order = self.wait_and_find_element(ConstructorLocators.ORDER_IN_HISTORY)
        order.click()

    @allure.step("получение окна заказа")
    def get_window(self):
        modal_window = self.wait_and_find_element(ConstructorLocators.MODAL_WINDOW)
        return modal_window

    @allure.step("закрытие окна")
    def close_window(self):
        close_icon = self.wait_and_find_element(ConstructorLocators.CROSS)
        close_icon.click()

    @allure.step("Формирвание бургера")
    def constructor_count(self):
        sauce = self.wait_and_find_element(ConstructorLocators.INGREDIENT)
        constructor = self.wait_and_find_element(ConstructorLocators.CONSTRUCTOR)
        self.drag_and_drop(sauce, constructor)

    @allure.step("Получение счётчика")
    def get_counter(self):
        count = self.wait_and_find_element(ConstructorLocators.COUNTER).text
        return count

    @allure.step("Авторизация")
    def authtorisation(self):
        auth = self.wait_and_find_element(ConstructorLocators.ENTER_ACCOUNT)
        auth.click()
        email = self.wait_and_find_element(ConstructorLocators.FIELD_AUTH_EMAIL)
        password = self.wait_and_find_element(ConstructorLocators.PASSWORD_AUTH_PASS)
        email.send_keys(TestData.EMAIL_ADRESS)
        password.send_keys(TestData.PASSWORD)
        auth = self.wait_and_find_element(ConstructorLocators.BUTTON_LOGIN)
        auth.click()

    @allure.step("добваление булок")
    def add_buns(self):
        sauce = self.wait_and_find_element(ConstructorLocators.BUNS)
        constructor = self.wait_and_find_element(ConstructorLocators.CONSTRUCTOR)
        self.drag_and_drop(sauce, constructor)

    @allure.step("Клик по кнопке заказа")
    def click_button_order(self):
        order = self.wait_and_find_element(ConstructorLocators.BUTTON_ORDER)
        order.click()

    @allure.step("Получение успешного заказа")
    def get_success_order(self):
        order = self.wait_and_find_element(ConstructorLocators.WINDOW_SUCCESS_ORDER)
        return order

    @allure.step("Переход на страницу аккаунта")
    def transition_to_pers_acc(self):
        personal_account = self.wait_and_find_element(ConstructorLocators.PERSONAL_ACCOUNT)
        personal_account.click()

    @allure.step("Переход на страницу истории")
    def transition_to_history(self):
        history = self.wait_and_find_element(ConstructorLocators.HISTORY_ORDER_LINK)
        history.click()

    @allure.step("Флоу заказа")
    def make_order_flow(self):
        sauce = self.wait_and_find_element(ConstructorLocators.BUNS)
        constructor = self.wait_and_find_element(ConstructorLocators.CONSTRUCTOR)
        self.drag_and_drop(sauce, constructor)
        click_order = self.wait_and_find_element(ConstructorLocators.BUTTON_ORDER)
        click_order.click()
        self.wait_and_find_element(ConstructorLocators.CROSS)

    @allure.step("Получение номера заказа")
    def get_number_of_order(self):
        number_of_order = self.wait_and_find_element(ConstructorLocators.NUMBER_OF_ORDER).text
        return int(number_of_order)

    @allure.step("Закрытие окна заказа")
    def close_order_window(self):
        close = self.wait_and_find_element(ConstructorLocators.CLOSE_ORDER_WINDOW)
        close.click()

    @allure.step("Получение номера заказа из истории заказаов")
    def get_number_of_order_in_history(self):
        number_history = self.wait_and_find_element(ConstructorLocators.NUMBER_ORDER_IN_HISTORY).text
        return number_history

    @allure.step("создание списка номеров заказов за всё время")
    def get_list_from_feed(self):
        list_oder_feed = []
        for element in self.wait_and_find_elements(ConstructorLocators.LIST_ORDER):
            list_oder_feed.append(element.text)
        return list_oder_feed

    @allure.step("получение счётчика заказов за всё время")
    def get_main_counter(self):
        first_counter = self.wait_and_find_element(ConstructorLocators.COUNTER_FOR_ALL_TIME).text
        return int(first_counter)

    @allure.step("получение счётчика заказов за день")
    def get_day_counter(self):
        second_counter = self.wait_and_find_element(ConstructorLocators.COUNTER_ORDER_TODAY).text
        return int(second_counter)

    @allure.step("получение номера заказа в работе")
    def get_number_order_in_work(self):
        in_work = self.wait_and_find_element(ConstructorLocators.NUMBER_OF_ORDER_IN_WORK).text
        return int(in_work)

    @allure.step("ожидание номера заказа")
    def wait_number_element(self):
        self.wait_and_find_element(ConstructorLocators.FIND_NUMBER_OF_ORDER)

