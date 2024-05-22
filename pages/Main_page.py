from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    _HEADERLOGOYANDEX=(By.XPATH,'//a[1][contains(@class, "Header_LogoYandex")]')
    _HEADERLOGOSCOOTER=(By.XPATH,'//a[2][contains(@class, "Header_LogoScooter")]')
    _HEADERBUTTONORDER=(By.XPATH,'//div[contains(@class, "Header_Nav")]//descendant::button[text()="Заказать"]')
    _HEADERBUTTONORDERSTATUS=(By.XPATH,'//div[contains(@class, "Header_Nav")]//descendant::button[text()="Статус заказа"]')
    _ORDERHEADERTEXT = (By.XPATH,'//div[contains(@class, "Order_Header")]')
    #_HOMEHEADERTEXT=''
    #_HOMESUBHEADERTEXT1=''
    #_HOMESUBHEADERTEXT2=''
    _HOMESUBHEADERTEXT3 =(By.XPATH, '//div[text()="Как это работает"]')
    _COOKIETEXT=(By.XPATH,'//div[contains(@class,"App_CookieText")]')
    _COOKIECONFIRMBUTTON=(By.XPATH,'//*[@id="rcc-confirm-button"]')
    _HOMESUBHEADER=(By.XPATH,'//*[@id="root"]/div/div/div[5]/div[contains(@class, "Home_SubHeader")]')
    _MIDDLEBUTTONORDER=(By.XPATH,'//button[contains(@class, "Button_Middle")]')
    _ACCORDIODIONBUTTON01=(By.XPATH,'//div[text()="Сколько это стоит? И как оплатить?"]')

    _ACCORDIODIONPANEL01=(By.XPATH,'//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]')
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
    #_IMIGESCOOTER=''
    def __init__(self,driver):
        #super.__init__(driver)
        self.driver=driver
    def ClickHeaderOrderButton(self):
        self.click_element(self._HEADERBUTTONORDER)

    def ClickMiddleOrderButton(self):
        self.click_element(self._MIDDLEBUTTONORDER)
    def ClickCoockieConfirmButton(self):
        self.click_element(self._COOKIECONFIRMBUTTON)


    def ClickAccordiodionButton01(self):
        self.click_element(self._ACCORDIODIONBUTTON01)

    def ClickAccordiodionButton02(self):
        self.click_element(self._ACCORDIODIONBUTTON02)
    def ClickAccordiodionButton03(self):
        self.click_element(self._ACCORDIODIONBUTTON03)
    def ClickAccordiodionButton04(self):
        self.click_element(self._ACCORDIODIONBUTTON04)
    def ClickAccordiodionButton05(self):
        self.click_element(self._ACCORDIODIONBUTTON05)
    def ClickAccordiodionButton06(self):
        self.click_element(self._ACCORDIODIONBUTTON06)

    def ClickAccordiodionButton07(self):
        self.click_element(self._ACCORDIODIONBUTTON07)
    def ClickAccordiodionButton08(self):
        self.click_element(self._ACCORDIODIONBUTTON08)
    def ShowTextAccordiopanel01(self):
        self.element_show_text(self._ACCORDIODIONPANEL01)

    def ShowTextAccordioPanel01(self):
        self.element_show_text(self._ACCORDIODIONPANEL01)

    def ShowTextAccordioPanel02(self):
        self.element_show_text(self._ACCORDIODIONPANEL02)

    def ShowTextAccordioPanel03(self):
        self.element_show_text(self._ACCORDIODIONPANEL03)

    def ShowTextAccordioPanel04(self):
        self.element_show_text(self._ACCORDIODIONPANEL04)

    def ShowTextAccordioPanel05(self):
        self.element_show_text(self._ACCORDIODIONPANEL05)

    def ShowTextAccordioPanel06(self):
        self.element_show_text(self._ACCORDIODIONPANEL06)

    def ShowTextAccordioPanel07(self):
        self.element_show_text(self._ACCORDIODIONPANEL07)

    def ShowTextAccordioPanel08(self):
        self.element_show_text(self._ACCORDIODIONPANEL08)
    def ClickLogoYandexHeader(self):
        self.click_element(self._HEADERLOGOYANDEX)
    def ClickLogoScooterHeader(self):
        self.click_element(self._HEADERLOGOSCOOTER)



