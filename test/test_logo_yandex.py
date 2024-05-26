import allure
from constants import Url
from pages.main_page import MainPage


class TestLogoYandex:
    @allure.title(' Проверка если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')  # декораторы
    @allure.description('В хедере нажимаем на логотип Яндекса и проверяем что открывается страница ДЗЕН')
    def test_click_yandex_logo(self,driver):
        Logo_yandex=MainPage(driver)
        Logo_yandex.click_logo_yandex_header()
        Logo_yandex.switch_to_window(driver)
        assert Logo_yandex.get_current_url() == Url.url_dzen
