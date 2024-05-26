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
    def input_name(self,name):
        self.enter_text(self._INPUTNAME,name)
    def input_surname(self,surname):
        self.enter_text(self._INPUTSURNAME,surname)
    def input_adress(self,adress):
        self.enter_text(self._INPUTADRESS,adress)
    def input_metro(self):
        self.click_element(self._INPUTMETRO)

    def choise_station_metro(self):
        self.click_element(self._LIST_SUBWAY_STATIONS)
    def input_telephone(self,phone):
        self.enter_text(self._INPUTPHONE,phone)
    def click_follow_button(self):
        self.click_element(self._FOLLOWBUTTON)
    def click_date_order(self):
        self.click_element(self._WHENBRINGSCOOTER)
    def choose_order_date(self):
        self.click_element(self._DATEPICKERDAY)
    def click_rental_period(self):
        self.click_element(self._RENTALPERIOD)
    def choose_rental_period_one_day(self):
        self.click_element(self._RENTALPERIODONEDAY)
    def choose_rental_period_two_day(self):
        self.click_element(self._RENTALPERIODTWODAY)

    def choose_color_black(self):
        self.click_element(self._SCOOTERCOLOURBLACK)
    def choose_color_grey(self):
        self.click_element(self._SCOOTERCOLOURGREY)
    def fill_comment_for_curier(self,comment):
        self.enter_text(self._COMMENTFORCOURIER,comment)
    def click_order_button(self):
        self.click_element(self._ORDERMIDDLEBUTTON)
    def go_next_step(self):
        self.find_element(self._ORDERMODALHEADER)
    def click_order_yes_button(self):
        self.click_element(self._YESBUTTON)
    def order_placed_text(self):
        self.find_element(self._ORDERHASBEENPLACED)


