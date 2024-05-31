import allure
from constants import Url
from pages.main_page import MainPage


class TestLogoYandex:
    @allure.title(' Проверка если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')  # декораторы
    @allure.description('В хедере нажимаем на логотип Яндекса и проверяем что открывается страница ДЗЕН')
    def test_click_yandex_logo(self,driver):
        logo_yandex=MainPage(driver)
        logo_yandex.click_logo_yandex_header()
        logo_yandex.switch_to_window(driver)
        with allure.step("Проверка фактического адреса открывшейся страницы с ожидаемым"):
            assert logo_yandex.get_current_url() == Url.url_dzen
