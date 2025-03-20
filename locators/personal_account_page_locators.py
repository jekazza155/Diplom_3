from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[text()='Вход']")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    ORDER_HISTORY_BTN = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BTN = (By.XPATH, "//button[text()='Выход']")
    DESCRIPTION_ACCOUNT = (By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")
    RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'][1]")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")