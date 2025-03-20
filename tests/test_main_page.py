import burger_api
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage
import allure


class TestMainPage:
    @allure.title("Переход на главную страницу через кнопку 'Конструктор'")
    @allure.description("Пользователь может перейти на главную страницу, нажав кнопку 'Конструктор' в шапке сайта.")
    def test_open_main_page_clicK_constructor_btn_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        order_list_page = OrderListPage(driver)
        main_page.click_list_order_button()
        order_list_page.click_constructor_button()
        current_url = order_list_page.check_main_page_url()
        assert current_url == True

    @allure.title("Переход на страницу 'Лента заказов'")
    @allure.description("Пользователь может перейти на страницу 'Лента заказов', нажав соответствующую кнопку в шапке сайта.")
    def test_open_list_order_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_list_order_button()
        current_url = main_page.check_order_list_url()
        assert current_url == True

    @allure.title("Открытие карточки ингредиента")
    @allure.description("При клике на ингредиент открывается всплывающее окно с детальной информацией о нем.")
    def test_open_ingredient_card_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient_button()
        assert main_page.check_ingredient_title() == True

    @allure.title("Закрытие карточки ингредиента")
    @allure.description("Всплывающее окно с информацией об ингредиенте закрывается при нажатии на кнопку 'Закрыть'.")
    def test_close_ingredient_card_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient_button()
        main_page.close_ingredient_card()
        assert main_page.check_main_page_title() == True

    @allure.title("Изменение счетчика ингредиента")
    @allure.description("Счетчик ингредиента увеличивается при добавлении его в конструктор бургера.")
    def test_change_counter_add_constructor_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        count_before = main_page.get_count_ingredient()
        main_page.add_bun_in_order()
        count_after = main_page.get_count_ingredient()
        assert count_before == '0' and count_after == '2'

    @allure.title("Оформление заказа авторизованным пользователем")
    @allure.description("Авторизованный пользователь может успешно оформить заказ через конструктор бургера.")
    def test_authorized_user_create_order_success(self, driver):
        user_data = burger_api.create_user_body()
        user_response = burger_api.create_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_enter_button()

        main_page.find_main_page_title()
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        description_create_order = main_page.find_create_order_description()
        access_token = burger_api.get_access_token(user_response)
        burger_api.delete_user(access_token)
        assert description_create_order.text == "Ваш заказ начали готовить"