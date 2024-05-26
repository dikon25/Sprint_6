import allure
from constants import Url
from helpers import QuestionsAnswers
from pages.main_page import MainPage
import pytest


class TestMainPage:
    @allure.title('Проверка точки входа в сценарий, кнопка «Заказать» вверху страницы.')  # декораторы
    @allure.description('В хедере кликаем кнопку "Заказать" и проверяем что открывается страница "https://qa-scooter.praktikum-services.ru/order"')
    def test_enter_from_header_button(self,driver):
        main_page=MainPage(driver)
        main_page.сlick_header_order_button()
        assert driver.current_url == Url.url_order

    @allure.title('Проверка точки входа в сценарий, кнопка «Заказать» в середине страницы.')  # декораторы
    @allure.description('В середине страницы кликаем кнопку "Заказать" и проверяем что открывается страница "https://qa-scooter.praktikum-services.ru/order"')
    def test_enter_from_middle_button(self,driver):
        main_page=MainPage(driver)
        main_page.сlick_coockie_confirm_button()
        main_page.сlick_middle_order_button()
        assert main_page.get_current_url() == Url.url_order

    @allure.title('Проверка на "https://qa-scooter.praktikum-services.ru/"Выпадающий список в разделе «Вопросы о важном»')  # декораторы
    @allure.description('Кликаем на вопросы и сравниваем ответы с документацией')

    @pytest.mark.parametrize('question, answer,assert_answer',MainPage.answers)
    def test_question_answer(self, driver,question, answer,assert_answer):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.сlick_coockie_confirm_button()
        main_page.click_question_main_page(question)
        text=main_page.answer_fact_result(answer)
        return text
        assert text == assert_answer
