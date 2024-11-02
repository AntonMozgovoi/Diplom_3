from selenium.webdriver.common.by import By
from data import TestData
from pages.basepage import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    def transition_to_account(self):  # переход на страницу авторизацию
        button = self.wait_and_find_element(MainPageLocators.ENTER_ACCOUNT)
        button.click()

    def transition_to_recovery(self):  #переход на страницу восстановления пароля
        link = self.wait_and_find_element(MainPageLocators.ENTER_RECOVERY_PASSWORD)
        link.click()

    def input_email(self):  #ввод почты для восстановления пароля
        field = self.wait_and_find_element(MainPageLocators.FIELD_INPUT_EMAIL)
        field.send_keys(TestData.EMAIL_ADRESS)



    def click_button_recover(self):  #поск кнопки восстановления пароля
        button = self.wait_and_find_element(MainPageLocators.BUTTON_RECOVER)
        button.click()

    def wait_element(self):  #поиск поля для ввода нового пароля
        self.wait_and_find_element(MainPageLocators.FIELD_NEW_PASSWORD)

    def select_password_field(self): #клик по полю ввода пароля
        field = self.wait_and_find_element(MainPageLocators.PASSWORD_FIELD)
        field.click()

    def transition_to_personal_account(self):
        button = self.wait_and_find_element(MainPageLocators.PERSONAL_ACCOUNT)
        button.click()

    def input_email_auth(self):
        email = self.wait_and_find_element(MainPageLocators.FIELD_AUTH_EMAIL)
        password = self.wait_and_find_element(MainPageLocators.PASSWORD_AUTH_PASS)
        email.send_keys(TestData.EMAIL_ADRESS)
        password.send_keys(TestData.PASSWORD)

    def login(self):
        button = self.wait_and_find_element(MainPageLocators.BUTTON_LOGIN)
        button.click()

    def transition_to_history(self):
        link = self.wait_and_find_element(MainPageLocators.HISTORY_ORDER_LINK)
        link.click()

    def logout(self):
        link = self.wait_and_find_element(MainPageLocators.LOGOUT_LINK)
        link.click()

    def find_element_logout(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_LOGIN)
