import allure
from selenium.webdriver.common.by import By
from data import TestData
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("переход на страницу авторизации")
    def transition_to_account(self):
        button = self.wait_and_find_element(MainPageLocators.ENTER_ACCOUNT)
        button.click()

    @allure.step("переход на страницу восстановления пароля")
    def transition_to_recovery(self):
        link = self.wait_and_find_element(MainPageLocators.ENTER_RECOVERY_PASSWORD)
        link.click()

    @allure.step("ввод почты для восстановления пароля")
    def input_email(self):
        field = self.wait_and_find_element(MainPageLocators.FIELD_INPUT_EMAIL)
        field.send_keys(TestData.EMAIL_ADRESS)

    @allure.step("поск кнопки восстановления пароля")
    def click_button_recover(self):
        button = self.wait_and_find_element(MainPageLocators.BUTTON_RECOVER)
        button.click()

    @allure.step("поиск поля для ввода нового пароля")
    def wait_element(self):
        self.wait_and_find_element(MainPageLocators.FIELD_NEW_PASSWORD)

    @allure.step("клик по полю ввода пароля")
    def select_password_field(self):
        field = self.wait_and_find_element(MainPageLocators.PASSWORD_FIELD)
        field.click()

    @allure.step("переход на страницу аккаунта")
    def transition_to_personal_account(self):
        button = self.wait_and_find_element(MainPageLocators.PERSONAL_ACCOUNT)
        button.click()

    @allure.step("ввод почты для авторизации")
    def input_email_auth(self):
        email = self.wait_and_find_element(MainPageLocators.FIELD_AUTH_EMAIL)
        password = self.wait_and_find_element(MainPageLocators.PASSWORD_AUTH_PASS)
        email.send_keys(TestData.EMAIL_ADRESS)
        password.send_keys(TestData.PASSWORD)

    @allure.step("нажатие кнопки авторизации")
    def login(self):
        button = self.wait_and_find_element(MainPageLocators.BUTTON_LOGIN)
        button.click()

    @allure.step("переход к странице истории")
    def transition_to_history(self):
        link = self.wait_and_find_element(MainPageLocators.HISTORY_ORDER_LINK)
        link.click()

    @allure.step("Выход")
    def logout(self):
        link = self.wait_and_find_element(MainPageLocators.LOGOUT_LINK)
        link.click()

    @allure.step("Ожидание кнопки логина")
    def find_element_logout(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_LOGIN)

    def get_type(self, driver):
        get_input = driver.find_element(By.NAME, "Пароль")
        return get_input

