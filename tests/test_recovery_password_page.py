from pages.main_page import MainPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.personal_account_page import PersonalAccountPage
from data import UserData
import allure


class TestRecoveryPassPage:
    @allure.title("Переход на страницу восстановления пароля")
    @allure.description("Пользователь может перейти на страницу восстановления пароля, нажав кнопку 'Восстановить пароль'.")
    def test_success_recovery_pass(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        assert recovery_page.check_recovery_page_title()

    @allure.title("Ввод почты и переход к восстановлению пароля")
    @allure.description("Пользователь может ввести почту и нажать кнопку 'Восстановить' для перехода к восстановлению пароля.")
    def test_input_email_and_click_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(UserData.USER_EMAIL)
        recovery_page.click_button_recovery()
        assert recovery_page.check_recovery_pass_title()

    @allure.title("Проверка работы кнопки 'Глазик' для отображения пароля")
    @allure.description("На странице восстановления пароля кнопка 'Глазик' позволяет отобразить скрытый пароль.")
    def test_eye_button_show_password_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(UserData.USER_EMAIL)
        recovery_page.click_button_recovery()
        recovery_page.set_new_password(UserData.NEW_PASSWORD)
        old_state = recovery_page.get_password_input_state()
        recovery_page.click_show_password_button()
        new_state = recovery_page.get_password_input_state()
        assert (old_state is False and new_state is True)