from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from constants import Url
from helpers import QuestionsAnswers


class MainPage(BasePage):
    _HEADERLOGOYANDEX=(By.XPATH,'//a[1][contains(@class, "Header_LogoYandex")]')
    _HEADERLOGOSCOOTER=(By.XPATH,'//a[2][contains(@class, "Header_LogoScooter")]')
    _HEADERBUTTONORDER=(By.XPATH,'//div[contains(@class, "Header_Nav")]//descendant::button[text()="Заказать"]')
    _HEADERBUTTONORDERSTATUS=(By.XPATH,'//div[contains(@class, "Header_Nav")]//descendant::button[text()="Статус заказа"]')
    _ORDERHEADERTEXT = (By.XPATH,'//div[contains(@class, "Order_Header")]')
    _HOMESUBHEADERTEXT3 =(By.XPATH, '//div[text()="Как это работает"]')
    _COOKIETEXT=(By.XPATH,'//div[contains(@class,"App_CookieText")]')
    _COOKIECONFIRMBUTTON=(By.XPATH,'//*[@id="rcc-confirm-button"]')
    _HOMESUBHEADER=(By.XPATH,'//*[@id="root"]/div/div/div[5]/div[contains(@class, "Home_SubHeader")]')
    _MIDDLEBUTTONORDER=(By.XPATH,'//button[contains(@class, "Button_Middle")]')
    _ACCORDIODIONBUTTON01=(By.XPATH,'//div[text()="Сколько это стоит? И как оплатить?"]')
    _ACCORDIODIONPANELAST = (By.XPATH, '(//div[text()="Я жизу за МКАДом, привезёте?"]')
    _ACCORDIODIONPANEL01=(By.XPATH,'//div[@id="accordion__panel-0"]//p')
    _ACCORDIODIONBUTTON02 =(By.XPATH, '//div[text()="Хочу сразу несколько самокатов! Так можно?"]')
    _ACCORDIODIONPANEL02 =(By.XPATH,'//p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]')
    _ACCORDIODIONBUTTON03 =(By.XPATH, '//div[text()="Как рассчитывается время аренды?"]')
    _ACCORDIODIONPANEL03 =(By.XPATH,'//p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]')
    _ACCORDIODIONBUTTON04 =(By.XPATH, '//div[text()="Можно ли заказать самокат прямо на сегодня?"]')
    _ACCORDIODIONPANEL04 =(By.XPATH,'//p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]')
    _ACCORDIODIONBUTTON05 =(By.XPATH, '//div[text()="Можно ли продлить заказ или вернуть самокат раньше?"]')
    _ACCORDIODIONPANEL05 =(By.XPATH,'//p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]')
    _ACCORDIODIONBUTTON06 =(By.XPATH, '//div[text()="Вы привозите зарядку вместе с самокатом?"]')
    _ACCORDIODIONPANEL06 =(By.XPATH,'//p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]')
    _ACCORDIODIONBUTTON07 =(By.XPATH, '//div[text()="Можно ли отменить заказ?"]')
    _ACCORDIODIONPANEL07 = (By.XPATH,'//p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]')
    _ACCORDIODIONBUTTON08 =(By.XPATH, '//div[text()="Я жизу за МКАДом, привезёте?"]')
    _ACCORDIODIONPANEL08 = (By.XPATH,'//p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]')

    answers = [
        [_ACCORDIODIONBUTTON01, _ACCORDIODIONPANEL01, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [_ACCORDIODIONBUTTON02, _ACCORDIODIONPANEL02,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [_ACCORDIODIONBUTTON03, _ACCORDIODIONPANEL03,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [_ACCORDIODIONBUTTON04, _ACCORDIODIONPANEL04,
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [_ACCORDIODIONBUTTON05, _ACCORDIODIONBUTTON05,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [_ACCORDIODIONBUTTON06, _ACCORDIODIONPANEL06,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [_ACCORDIODIONBUTTON07, _ACCORDIODIONPANEL07,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [_ACCORDIODIONBUTTON08, _ACCORDIODIONPANEL08,
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.']]

    def __init__(self,driver):
        #super.__init__(driver)
        self.driver=driver
    def сlick_header_order_button(self):
        self.click_element(self._HEADERBUTTONORDER)

    def сlick_middle_order_button(self):
        self.click_element(self._MIDDLEBUTTONORDER)
    def сlick_coockie_confirm_button(self):
        self.click_element(self._COOKIECONFIRMBUTTON)

    def click_logo_yandex_header(self):
        self.click_element(self._HEADERLOGOYANDEX)
    def click_logo_scooter_header(self):
        self.click_element(self._HEADERLOGOSCOOTER)
    def open_page_for_scooter(self):
        self.navigate(Url.url_order)
    def button_scooter_visible(self):
        self.wait_for_element_visible(self._HEADERLOGOSCOOTER)
    def switch_to_window(self, driver):
         self.driver.switch_to.window(driver.window_handles[1])

    def get_current_url(self):
        return self.driver.current_url

    def check_redirection_on_scooter_page(self):
        self.cross_url(Url.url_main)

    def go_to_main_page(self):
        self.navigate(Url.url_main)
    def click_question_main_page(self,question):
        self.click_element(question)

    def answer_fact_result(self,answer):
        return self.element_show_text(answer)



