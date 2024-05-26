import allure
from constants import Url
from pages.main_page import MainPage


class TestLogoScooter:
    @allure.title('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')  # декораторы
    @allure.description('на странице "https://qa-scooter.praktikum-services.ru/order" кликаем на логотип Самокат и проверяем что открывается страница https://qa-scooter.praktikum-services.ru/')
    def test_click_scooter_logo(self,driver):
        Logo_scooter=MainPage(driver)
        Logo_scooter.сlick_coockie_confirm_button()
        Logo_scooter.сlick_header_order_button()
        Logo_scooter.open_page_for_scooter()
        Logo_scooter.click_logo_scooter_header()
        Logo_scooter.check_redirection_on_scooter_page()
        assert Logo_scooter.get_current_url() == Url.url_main