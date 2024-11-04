import allure
from selenium.webdriver.common.by import By
from data import Urls
from locators import MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestLogoScooter:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transition_on_recovery_page(self, driver):
        transition = MainPage(driver)
        transition.transition_to_account()
        transition.transition_to_recovery()
        assert driver.current_url == Urls.RECOV_PASS_PAGE

    @allure.title('Проверка ввода почты')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_input_mail_click_recover(self, driver):
        recover = MainPage(driver)
        recover.transition_to_account()
        recover.transition_to_recovery()
        recover.input_email()
        recover.click_button_recover()
        recover.wait_element()
        assert driver.current_url == Urls.RESET_PASS_PAGE

    @allure.title('Проверка кнопки показать пароль')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_field(self, driver):
        field = MainPage(driver)
        field.transition_to_account()
        field.select_password_field()
        input_field = driver.find_element(By.NAME, "Пароль")
        assert input_field.get_attribute('type') == 'text'