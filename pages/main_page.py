import allure
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
    _ACCORDIODIONBUTTON01=(By.XPATH,'//div[@id = "accordion__heading-0"]')
    _ACCORDIODIONPANEL01=(By.XPATH,'//div[@id="accordion__panel-0"]//p')
    _ACCORDIODIONBUTTON02 =(By.XPATH, '//div[@id = "accordion__heading-1"]')
    _ACCORDIODIONPANEL02 =(By.XPATH,'//div[@id="accordion__panel-1"]//p')
    _ACCORDIODIONBUTTON03 =(By.XPATH, '//div[@id = "accordion__heading-2"]')
    _ACCORDIODIONPANEL03 =(By.XPATH,'//div[@id="accordion__panel-2"]//p')
    _ACCORDIODIONBUTTON04 =(By.XPATH, '//div[@id = "accordion__heading-3"]')
    _ACCORDIODIONPANEL04 =(By.XPATH,'//div[@id="accordion__panel-3"]//p')
    _ACCORDIODIONBUTTON05 =(By.XPATH, '//div[@id = "accordion__heading-4"]')
    _ACCORDIODIONPANEL05 =(By.XPATH,'//div[@id="accordion__panel-4"]//p')
    _ACCORDIODIONBUTTON06 =(By.XPATH, '//div[@id = "accordion__heading-5"]')
    _ACCORDIODIONPANEL06 =(By.XPATH,'//div[@id="accordion__panel-5"]//p')
    _ACCORDIODIONBUTTON07 =(By.XPATH, '//div[@id = "accordion__heading-6"]')
    _ACCORDIODIONPANEL07 = (By.XPATH,'//div[@id="accordion__panel-6"]//p')
    _ACCORDIODIONBUTTON08 =(By.XPATH, '//div[@id = "accordion__heading-7"]')
    _ACCORDIODIONPANEL08 = (By.XPATH,'//div[@id="accordion__panel-7"]//p')

    answers = [
        [_ACCORDIODIONBUTTON01, _ACCORDIODIONPANEL01, QuestionsAnswers.assert_answer[0]],
        [_ACCORDIODIONBUTTON02, _ACCORDIODIONPANEL02, QuestionsAnswers.assert_answer[1]],
        [_ACCORDIODIONBUTTON03, _ACCORDIODIONPANEL03,QuestionsAnswers.assert_answer[2]],
        [_ACCORDIODIONBUTTON04, _ACCORDIODIONPANEL04,QuestionsAnswers.assert_answer[3]],
        [_ACCORDIODIONBUTTON05, _ACCORDIODIONPANEL05,QuestionsAnswers.assert_answer[4]],
        [_ACCORDIODIONBUTTON06, _ACCORDIODIONPANEL06,QuestionsAnswers.assert_answer[5]],
        [_ACCORDIODIONBUTTON07, _ACCORDIODIONPANEL07,QuestionsAnswers.assert_answer[6]],
        [_ACCORDIODIONBUTTON08, _ACCORDIODIONPANEL08,QuestionsAnswers.assert_answer[7]]]

    @allure.step('Запуск браузера')
    def __init__(self,driver):
        self.driver=driver

    @allure.step('Кликнуть по кнопке "ЗАКАЗАТЬ" в хедере')
    def сlick_header_order_button(self):
        self.click_element(self._HEADERBUTTONORDER)

    @allure.step('Кликнуть по кнопке ЗАКАЗАТЬ в середине страницы')
    def сlick_middle_order_button(self):
       self.click_element(self._MIDDLEBUTTONORDER)

    @allure.step('Кликнуть по кнопке "Согласится с куками"')
    def сlick_coockie_confirm_button(self):
        self.click_element(self._COOKIECONFIRMBUTTON)

    @allure.step('Кликнуть по логотипу "Яндекс" в хедере')
    def click_logo_yandex_header(self):
        self.click_element(self._HEADERLOGOYANDEX)

    @allure.step('Кликнуть по логотипу "Самокат" в хедере')
    def click_logo_scooter_header(self):
        self.click_element(self._HEADERLOGOSCOOTER)

    @allure.step('Открыть страницу заказа')
    def open_page_order(self):
        self.navigate(Url.url_order)

    @allure.step('Перейти на главную страницу')
    def go_to_main_page(self):
        self.navigate(Url.url_main)

    @allure.step('Нажать на вопрос внизу главной страницы')
    def click_question_main_page(self,question):
        self.click_element(question)

    @allure.step('Показать ответ на вопрос')
    def answer_fact_result(self,answer):
        return self.element_show_text(answer)


