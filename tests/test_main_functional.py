import time
import allure
from data import Urls
from locators import OrderFeed
from pages.constructor import Constructor
from pages.mainpage import MainPage


class TestConstructor:
    @allure.title('переход по клику на «Конструктор»')
    @allure.description('Успешный переход на страницу конструктора')
    def test_transition_constructor(self, driver):
        const = Constructor(driver)
        const.transition_to_constructor()
        assert driver.current_url == Urls.MAIN_PAGE

    @allure.title('переход по клику на «Лента заказов»')
    @allure.description('Успешный переход на страницу заказов')
    def test_transition_order_list(self, driver):
        feed = Constructor(driver)
        feed.transition_to_order_list()
        assert driver.current_url == Urls.FEED_ORDER

    @allure.title('Проверка окна с деталями')
    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_window_detail(self, driver):
        window = Constructor(driver)
        window.transition_to_order_list()
        window.select_order_from_feed()
        modal_window = window.get_window()
        assert modal_window.is_displayed()

    @allure.title('Проверка закрытия окна')
    @allure.description('всплывающее окно закрывается кликом по крестику')
    def test_close_window(self, driver):
        window = Constructor(driver)
        window.transition_to_order_list()
        window.select_order_from_feed()
        window.close_window()
        modal_window = window.get_window()
        time.sleep(3)
        assert not modal_window.is_displayed()

    @allure.title('Проверка каунтера ингридиента')
    @allure.description('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_count(self, driver):
        window = Constructor(driver)
        window.constructor_count(driver)
        count = window.get_counter()
        assert count == '1'

    @allure.title('Проверка заказа')
    @allure.description('залогиненный пользователь может оформить заказ')
    def test_order_flow(self, driver):
        order_flow = Constructor(driver)
        order_flow.authtorisation()
        order_flow.add_buns(driver)
        order_flow.constructor_count(driver)
        order_flow.click_button_order()
        order = order_flow.get_success_order()
        assert order.is_displayed
