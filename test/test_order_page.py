import allure
import pytest
from helpers import RegData
from pages.order_page import OrderPage
from pages.main_page import MainPage


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

    def test_input_form_1(self,driver,name,surname,address,phone,comment):
        order_page = OrderPage(driver)
        main_page=MainPage(driver)
        main_page.сlick_coockie_confirm_button()
        main_page.сlick_header_order_button()
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_adress(address)
        order_page.input_metro()
        order_page.choise_station_metro()
        order_page.input_telephone(phone)
        order_page.click_follow_button()
        order_page.click_date_order()
        order_page.choose_order_date()
        order_page.click_rental_period()
        order_page.choose_rental_period_one_day()
        order_page.choose_color_black()
        order_page.fill_comment_for_curier(comment)
        order_page.click_order_button()
        order_page.go_next_step()
        order_page.click_order_yes_button()
        OrderPlaced=order_page.order_placed_text()
        return OrderPlaced
        assert OrderPlaced






