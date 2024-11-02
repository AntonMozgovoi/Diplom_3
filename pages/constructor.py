import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from conftest import driver
from data import TestData
from locators import Header, OrderFeed, MainPageLocators
from pages.basepage import BasePage
from pages.mainpage import MainPage


class Constructor(BasePage):
    def transition_to_constructor(self):  # переход на страницу конструктор
        const = self.wait_and_find_element(Header.CONSTRUCTOR)
        const.click()

    def transition_to_order_list(self): # переход на страницу заказов
        order_list = self.wait_and_find_element(Header.ORDER_LIST)
        order_list.click()

    def select_order_from_feed(self): # выбор заказа из ленты заказов
        order = self.wait_and_find_element(OrderFeed.ORDER_IN_HISTORY)
        order.click()

    def get_window(self): # получение окна заказа
        modal_window = self.wait_and_find_element(OrderFeed.MODAL_WINDOW)
        return modal_window

    def close_window(self): # закрытие окна
        close_icon = self.wait_and_find_element(OrderFeed.CROSS)
        close_icon.click()

    def constructor_count(self, driver):
        sauce = self.wait_and_find_element(OrderFeed.INGREDIENT)
        constructor = self.wait_and_find_element(OrderFeed.CONSTRUCTOR)
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(sauce, constructor).perform()

    def get_counter(self):
        count = self.wait_and_find_element(OrderFeed.COUNTER).text
        return count

    def authtorisation(self): # авторизация
        auth = self.wait_and_find_element(MainPageLocators.ENTER_ACCOUNT)
        auth.click()
        email = self.wait_and_find_element(MainPageLocators.FIELD_AUTH_EMAIL)
        password = self.wait_and_find_element(MainPageLocators.PASSWORD_AUTH_PASS)
        email.send_keys(TestData.EMAIL_ADRESS)
        password.send_keys(TestData.PASSWORD)
        auth = self.wait_and_find_element(MainPageLocators.BUTTON_LOGIN)
        auth.click()

    def add_buns(self, driver):
        sauce = self.wait_and_find_element(OrderFeed.BUNS)
        constructor = self.wait_and_find_element(OrderFeed.CONSTRUCTOR)
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(sauce, constructor).perform()

    def click_button_order(self):
        order = self.wait_and_find_element(OrderFeed.BUTTON_ORDER)
        order.click()

    def get_success_order(self):
        order = self.wait_and_find_element(OrderFeed.WINDOW_SUCCESS_ORDER)
        return order

    def transition_to_pers_acc(self):
        personal_account = self.wait_and_find_element(MainPageLocators.PERSONAL_ACCOUNT)
        personal_account.click()

    def transition_to_history(self):
        history = self.wait_and_find_element(MainPageLocators.HISTORY_ORDER_LINK)
        history.click()

    def make_order_flow(self, driver):
        sauce = self.wait_and_find_element(OrderFeed.BUNS)
        constructor = self.wait_and_find_element(OrderFeed.CONSTRUCTOR)
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(sauce, constructor).perform()
        click_order = self.wait_and_find_element(OrderFeed.BUTTON_ORDER)
        click_order.click()

    def get_number_of_order(self):  # Получение номера заказа
        number_of_order = self.wait_and_find_element(OrderFeed.NUMBER_OF_ORDER).text
        return int(number_of_order)

    def close_order_window(self):
        close = self.wait_and_find_element(OrderFeed.CLOSE_ORDER_WINDOW)
        close.click()

    def get_number_of_order_in_history(self):
        number_history = self.wait_and_find_element(OrderFeed.NUMBER_ORDER_IN_HISTORY).text
        return number_history

    def find_number_in_feed(self, driver):
        text = Constructor.get_number_of_order_in_history(self)
        return text

    def get_list_from_feed(self, driver):   # создание списка номеров заказов за всё время
        list_oder_feed = []
        for element in driver.find_elements(By.XPATH, '//*[@Class="text text_type_digits-default"]'):
            list_oder_feed.append(element.text)
        return list_oder_feed

    def get_main_counter(self):  # получение счётчика заказов за всё время
        first_counter = self.wait_and_find_element(OrderFeed.COUNTER_FOR_ALL_TIME).text
        return int(first_counter)

    def get_day_counter(self):  # получение счётчика заказов за день
        second_counter = self.wait_and_find_element(OrderFeed.COUNTER_ORDER_TODAY).text
        return int(second_counter)

    def get_number_order_in_work(self): # получение номера заказа "в работе"
        in_work = self.wait_and_find_element(OrderFeed.NUMBER_OF_ORDER_IN_WORK).text
        return int(in_work)