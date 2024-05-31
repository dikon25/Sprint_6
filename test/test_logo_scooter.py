import allure
from constants import Url
from pages.main_page import MainPage


class TestLogoScooter:
    @allure.title('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')  # декораторы
    @allure.description('на странице "https://qa-scooter.praktikum-services.ru/order" кликаем на логотип Самокат и проверяем что открывается страница https://qa-scooter.praktikum-services.ru/')
    def test_click_scooter_logo(self,driver):
            logo_scooter=MainPage(driver)
            logo_scooter.open_page_order()
            logo_scooter.сlick_coockie_confirm_button()
            logo_scooter.click_logo_scooter_header()
            with allure.step("Проверка фактического адреса открывшейся страницы с ожидаемым"):
                assert logo_scooter.get_current_url() == Url.url_main