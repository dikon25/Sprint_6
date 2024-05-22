import allure
import pytest
from config import *
from pages.Order_page import OrderPage
from pages.Main_page import MainPage


class TestOrderPage:
    @allure.title(
        'Проверка позитивного сценария заказа самоката на странице "https://qa-scooter.praktikum-services.ru/order"')  # декораторы
    @allure.description(
        'Заполняем регистрационные формы разными наборами данных два раза.Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа. "')


    @pytest.mark.parametrize('name,surname,address,phone,comment',[[RegData.Reg_up_data_name(),
                                                                    RegData.Reg_up_data_surname(),
                                                                    RegData.Reg_up_data_address(),
                                                                    RegData.Reg_up_data_phone(),
                                                                    RegData.Reg_up_data_comment()],
                                                                   [RegData.Reg_up_data_name(),
                                                                    RegData.Reg_up_data_surname(),
                                                                    RegData.Reg_up_data_address(),
                                                                    RegData.Reg_up_data_phone(),
                                                                     RegData.Reg_up_data_comment()]])

    def testInputForm1(self,driver,name,surname,address,phone,comment):
        order_page = OrderPage(driver)
        main_page=MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickHeaderOrderButton()
        order_page.InputName(name)
        order_page.InputSurname(surname)
        order_page.InputAdress(address)
        order_page.InputMetro()
        order_page.ChoiseStationMetro()
        order_page.InputTelephone(phone)
        order_page.ClickFollowButton()
        order_page.ClickDateOrder()
        order_page.ChooseOrderDate()
        order_page.ClickRentalPeriod()
        order_page.ChooseRentalPeriodOneDay()
        order_page.ChooseColorBlack()
        order_page.FillCommentForCurier(comment)
        order_page.ClickOrderButton()
        order_page.GoNextStep()
        order_page.ClickOrderYesButton()
        OrderPlaced=order_page.OrderPlacedText()
        return OrderPlaced
        assert OrderPlaced






