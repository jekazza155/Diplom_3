from selenium.webdriver.common.by import By

class RecoveryPassPageLocators:
    BUTTON_RECOVERY = (By.XPATH, "//button[text() = 'Восстановить']")
    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    RECOVER_PASS_TITLE = (By.XPATH, "//h2[text()= 'Восстановление пароля']")
    EYE_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    BUTTON_ACCOUNT = (By.XPATH, "(.//a[@class = 'AppHeader_header__link__3D_hX'])[2]")
    RECOVER_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    FIELD_NEW_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")
    PASSWORD_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'")