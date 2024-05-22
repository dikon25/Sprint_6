from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    _ORDERHEADERTEXT=(By.XPATH,'//div[contains(@class, "Order_Header")]')
    _INPUTNAME=(By.XPATH,'//input[contains(@placeholder,"* Имя")]')
    _ERRORNAME=(By.XPATH,'//input[contains(@placeholder,"* Имя")]//following-sibling::div')
    _INPUTSURNAME = (By.XPATH,'//input[contains(@placeholder,"* Фамилия")]')
    _ERRORSURNAME = (By.XPATH,'//input[contains(@placeholder,"* Фамилия")]//following-sibling::div')
    _INPUTADRESS = (By.XPATH,'//input[contains(@placeholder,"* Адрес: куда привезти заказ")]')
    _ERRORADRESS = (By.XPATH,'//input[contains(@placeholder,"* Адрес: куда привезти заказ")]//following-sibling::div')
    _INPUTMETRO = (By.XPATH,'//input[contains(@placeholder,"* Станция метро")]')
    _LIST_SUBWAY_STATIONS = (By.XPATH, './/li[@data-value="1"]')

    _METRO2=(By.XPATH,'//input[contains(@value,"Беляево")]')
    _ERRORMETRO = (By.XPATH,'//input[contains(@placeholder,"* Станция метро")]//following-sibling::div')
    _INPUTPHONE = (By.XPATH,'//input[contains(@placeholder,"* Телефон: на него позвонит курьер")]')
    _ERRORPHONE = (By.XPATH,'//input[contains(@placeholder,"* Телефон: на него позвонит курьер")]//following-sibling::div')
    _FOLLOWBUTTON=(By.XPATH,'//button[text()="Далее"]')#div[contains(@class, "Order_NextButton")]//descendant::button')#//div[contains(@class, "Order_NextButton")]//descendant::button
    _WHENBRINGSCOOTER=(By.XPATH,'//input[contains(@placeholder,"* Когда привезти самокат")]')
    _DATEPICKERDAY=(By.XPATH,'//div[contains(@aria-label,"Choose четверг, 23-е мая 2024 г.")]')
    _RENTALPERIOD=(By.XPATH,'//div[contains(@class, "Dropdown-root")]')
    _RENTALPERIODONEDAY=(By.XPATH,'//div[text()="сутки"]')
    _RENTALPERIODTWODAY = (By.XPATH,'//div[text()="двое суток"]')
    _RENTALPERIODTHREEDAY =(By.XPATH, '//div[text()="трое суток"]')
    _RENTALPERIODFOURDAY = (By.XPATH,'//div[text()="четверо суток"]')
    _RENTALPERIODFIVEDAY =(By.XPATH, '//div[text()="пятеро суток"]')
    _RENTALPERIODSIXDAY =(By.XPATH, '//div[text()="шестеро суток"]')
    _RENTALPERIODSEVENDAY = (By.XPATH,'//div[text()="семеро суток"]')
    _SCOOTERCOLOURBLACK=(By.XPATH,'// *[ @ id = "black"]')
    _SCOOTERCOLOURGREY=(By.XPATH,'// *[ @ id = "grey"]')
    _COMMENTFORCOURIER=(By.XPATH,'//input[contains(@placeholder,"Комментарий для курьера")]')
    _BACKBUTTON=(By.XPATH,'//div[contains(@class, "Order_Button")]//descendant::button[text()="Назад"]')
    _ORDERMIDDLEBUTTON=(By.XPATH,'//div[contains(@class, "Order_Button")]//descendant::button[text()="Заказать"]')
    _ORDERMODALHEADER=(By.XPATH,'//div[contains(@class, "Order_ModalHeader")]')
    _NOBUTTON=(By.XPATH,'//div[contains(@class, "Order_Buttons")]//descendant::button[text()="Нет"]')
    _YESBUTTON=(By.XPATH,'//div[contains(@class, "Order_Buttons")]//descendant::button[text()="Да"]')
    _ORDERHASBEENPLACED=(By.XPATH,'//div[contains(@class,"Order_ModalHeader")]')
    _ORDERVALUETEXT=(By.XPATH,'//div[contains(@class,"Order_Text")]')
    _SHOWSTATUSBUTTON=(By.XPATH,'//div[contains(@class, "Order_NextButton")]//descendant::button')
    def __init__(self,driver):
        #super.__init__(driver)
        self.driver=driver
    def InputName(self,name):
        self.enter_text(self._INPUTNAME,name)
    def InputSurname(self,surname):
        self.enter_text(self._INPUTSURNAME,surname)
    def InputAdress(self,adress):
        self.enter_text(self._INPUTADRESS,adress)
    def InputMetro(self):
        self.click_element(self._INPUTMETRO)

    def ChoiseStationMetro(self):
        self.click_element(self._LIST_SUBWAY_STATIONS)
    def InputTelephone(self,phone):
        self.enter_text(self._INPUTPHONE,phone)
    def ClickFollowButton(self):
        self.click_element(self._FOLLOWBUTTON)
    def ClickDateOrder(self):
        self.click_element(self._WHENBRINGSCOOTER)
    def ChooseOrderDate(self):
        self.click_element(self._DATEPICKERDAY)
    def ClickRentalPeriod(self):
        self.click_element(self._RENTALPERIOD)
    def ChooseRentalPeriodOneDay(self):
        self.click_element(self._RENTALPERIODONEDAY)
    def ChooseRentalPeriodTwoDay(self):
        self.click_element(self._RENTALPERIODTWODAY)

    def ChooseColorBlack(self):
        self.click_element(self._SCOOTERCOLOURBLACK)
    def ChooseColorGrey(self):
        self.click_element(self._SCOOTERCOLOURGREY)
    def FillCommentForCurier(self,comment):
        self.enter_text(self._COMMENTFORCOURIER,comment)
    def ClickOrderButton(self):
        self.click_element(self._ORDERMIDDLEBUTTON)
    def GoNextStep(self):
        self.element_is_present(self._ORDERMODALHEADER)
    def ClickOrderYesButton(self):
        self.click_element(self._YESBUTTON)
    def OrderPlacedText(self):
        self.element_is_present(self._ORDERHASBEENPLACED)


