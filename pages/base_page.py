from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента и его поиск по локатору: {locator}")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Открытие страницы по URL: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Проверка наличия элемента на странице по локатору: {locator} с таймаутом {timeout} секунд")
    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Клик по элементу с использованием JavaScript по локатору: {locator}")
    def click_element(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)