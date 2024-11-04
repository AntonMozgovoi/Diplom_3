import allure
from data import Urls
from locators import MainPageLocators
from pages.main_page import MainPage

class TestPersonalAccount:
    @allure.title('Проверка перехода в личный кабинет')
    @allure.description('переход по клику на «Личный кабинет»')
    def test_transition_to_personal_account(self, driver):
        transition = MainPage(driver)
        transition.transition_to_personal_account()
        transition.select_password_field()
        assert driver.current_url == Urls.PERSONAL_ACCOUNT

    @allure.title('Проверка перехода на страницу "История заказов')
    @allure.description('переход в раздел «История заказов»')
    def test_transition_story_orders(self, driver):
        transition = MainPage(driver)
        transition.transition_to_account()
        transition.input_email_auth()
        transition.login()
        transition.transition_to_personal_account()
        transition.transition_to_history()
        assert driver.current_url == Urls.HISTORY_ORDER

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('выход из аккаунта')
    def test_logout(self, driver):
        transition = MainPage(driver)
        transition.transition_to_personal_account()
        transition.input_email_auth()
        transition.login()
        transition.transition_to_personal_account()
        transition.logout()
        transition.find_element_logout()
        assert driver.current_url == Urls.PERSONAL_ACCOUNT

