import allure
from config import Url
from pages.Main_page import MainPage

class TestLogoScooter:
    @allure.title('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')  # декораторы
    @allure.description('на странице "https://qa-scooter.praktikum-services.ru/order" кликаем на логотип Самокат и проверяем что открывается страница https://qa-scooter.praktikum-services.ru/')
    def testClickScooterLogo(self,driver):
        Logo_scooter=MainPage(driver)
        Logo_scooter.navigate(Url.url_order)
        Logo_scooter.ClickLogoScooterHeader()
        assert driver.current_url == Url.url_main