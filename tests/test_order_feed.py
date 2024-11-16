import allure
from pages.constructor_page import Constructor


class TestOrderFeed:
    @allure.title('Выбор заказа')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_select_order(self, driver):
        select_order = Constructor(driver)
        select_order.transition_to_order_list()
        select_order.select_order_from_feed()
        order = select_order.get_window()
        assert order.is_displayed

    @allure.title('Отображение заказов в ленте')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_in_order_feed(self, driver):
        display_order = Constructor(driver)
        display_order.authtorisation()
        display_order.make_order_flow()
        display_order.wait_number_element()
        display_order.close_order_window()
        display_order.transition_to_pers_acc()
        display_order.transition_to_history()
        number_in_history = display_order.get_number_of_order_in_history()
        display_order.transition_to_order_list()
        list_feed = display_order.get_list_from_feed()
        assert number_in_history in list_feed

    @allure.title('Проверка счётчик Выполнено за всё время')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_all_time(self, driver):
        at_counter = Constructor(driver)
        at_counter.authtorisation()
        at_counter.transition_to_order_list()
        first_number = at_counter.get_main_counter()
        at_counter.transition_to_constructor()
        at_counter.make_order_flow()
        at_counter.wait_number_element()
        at_counter.close_order_window()
        at_counter.transition_to_order_list()
        second_number = at_counter.get_main_counter()
        assert first_number < second_number

    @allure.title('Проверка счётчик Выполнено за сегодня')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается,')
    def test_counter_today(self, driver):
        today_counter = Constructor(driver)
        today_counter.authtorisation()
        today_counter.transition_to_order_list()
        first_number = today_counter.get_day_counter()
        today_counter.transition_to_constructor()
        today_counter.make_order_flow()
        today_counter.wait_number_element()
        today_counter.close_order_window()
        today_counter.transition_to_order_list()
        second_number = today_counter.get_day_counter()
        assert first_number < second_number

    @allure.title('Проверка отображения заказа в разделе "В работе"')
    @allure.description('после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver):
        in_work = Constructor(driver)
        in_work.authtorisation()
        in_work.make_order_flow()
        in_work.wait_number_element()
        number = in_work.get_number_of_order()
        in_work.close_order_window()
        in_work.transition_to_order_list()
        order = in_work.get_number_order_in_work()
        assert number == order
