from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    @allure.step('Запуск браузера')
    def __init__(self,driver:WebDriver):
        self.driver=driver

    @allure.step('Перейти на страницу')
    def navigate(self,url:str):
        self.driver.get(url)

    @allure.step('Получить адрес страницы в новом окне')
    def switch_to_window(self,driver):
        self.driver.switch_to.window(driver.window_handles[1])

    @allure.step('Найти элемент')
    def find_element(self,locator:tuple,timeout:int=10):
        self.driver.find_element(*locator)
        try:
            return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Element with Locator{locator} not found within {timeout} seconds')
            return None

    @allure.step('Найти элементы')
    def find_elements(self,locator:tuple,timeout:int=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f'Element with Locator{locator} not found within {timeout} seconds')
            return []

    @allure.step('Нажать на элемент')
    def click_element(self,locator:tuple,timeout:int=10):
        element=self.find_element(locator,timeout)
        if element:
            element.click()
        else:
            print(f'Failed to click of element with locator{locator}')

    @allure.step('Ввести текс')
    def enter_text(self,locator:tuple,text:str,timeout:int=10):
        element=self.find_element(locator,timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Failed to enter text in element with locator {locator}')

    @allure.step('Дождатся видимости элемента')
    def wait_for_element_visible(self,locator:tuple,timeout:int=10):
        try:
            return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not visible after {timeout} seconds')
            return None

    @allure.step('Вывести текст')

    def element_show_text(self,locator:tuple,timeout: int=10):
        return self.find_element(locator,timeout).text

    @allure.step('Получить адрес текущей страницы')
    def get_current_url(self):
        return self.driver.current_url




