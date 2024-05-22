import allure
from config import Url
from pages.Main_page import MainPage

class TestLogoYandex:
    @allure.title(' Проверка если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')  # декораторы
    @allure.description('В хедере нажимаем на логотип Яндекса и проверяем что открывается страница ДЗЕН')
    def testClickYandexLogo(self,driver):
        Logo_yandex=MainPage(driver)
        Logo_yandex.ClickLogoYandexHeader()
        driver.switch_to.window(driver.window_handles[1])
        url = driver.current_url
        assert url == Url.url_dzen
