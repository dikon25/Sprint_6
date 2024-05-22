import allure
from config import Url
from pages.Main_page import MainPage


class TestMainPage:
    @allure.title('Проверка точки входа в сценарий, кнопка «Заказать» вверху страницы.')  # декораторы
    @allure.description('В хедере кликаем кнопку "Заказать" и проверяем что открывается страница "https://qa-scooter.praktikum-services.ru/order"')
    def testEnterFromHeaderButton(self,driver):
        main_page=MainPage(driver)
        main_page.ClickHeaderOrderButton()
        assert driver.current_url == Url.url_order

    @allure.title('Проверка точки входа в сценарий, кнопка «Заказать» в середине страницы.')  # декораторы
    @allure.description('В середине страницы кликаем кнопку "Заказать" и проверяем что открывается страница "https://qa-scooter.praktikum-services.ru/order"')
    def testEnterFromMiddleButton(self,driver):
        main_page=MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickMiddleOrderButton()
        assert driver.current_url == Url.url_order

    @allure.title('Проверка на "https://qa-scooter.praktikum-services.ru/"Выпадающий список в разделе «Вопросы о важном»')  # декораторы
    @allure.description('Кликаем на вопрос"Сколько это стоит? И как оплатить?" додлжен получить ответ "Сутки — 400 рублей. Оплата курьеру — наличными или картой."')
    def testDropDownListQuestion1(self,driver):
        main_page = MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickAccordiodionButton01()
        text=main_page.ShowTextAccordioPanel01()
        return text
        assert text=="Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    @allure.title('Проверка на "https://qa-scooter.praktikum-services.ru/" Выпадающий список в разделе «Вопросы о важном» ')  # декораторы
    @allure.description('Кликаем на вопрос"Хочу сразу несколько самокатов! Так можно?" должен получить ответ "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."')

    def testDropDownListQuestion2(self,driver):
        main_page = MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickAccordiodionButton02()
        text=main_page.ShowTextAccordioPanel02()
        return text
        assert text=="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    @allure.title('Проверка на "https://qa-scooter.praktikum-services.ru/" Выпадающий список в разделе «Вопросы о важном» ')  # декораторы
    @allure.description('Кликаем на вопрос"Как рассчитывается время аренды?" должен получить ответ "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."')

    def testDropDownListQuestion3(self,driver):
        main_page = MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickAccordiodionButton03()
        text=main_page.ShowTextAccordioPanel03()
        return text
        assert text=="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title('Проверка на "https://qa-scooter.praktikum-services.ru/" Выпадающий список в разделе «Вопросы о важном»')  # декораторы
    @allure.description('Можно ли заказать самокат прямо на сегодня?" должен получить ответ "Только начиная с завтрашнего дня. Но скоро станем расторопнее."')

    def testDropDownListQuestion4(self,driver):
        main_page = MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickAccordiodionButton04()
        text=main_page.ShowTextAccordioPanel04()
        return text
        assert text=="Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    @allure.title('Проверка на"https://qa-scooter.praktikum-services.ru/" Выпадающий список в разделе «Вопросы о важном»')  # декораторы
    @allure.description('На вопрос"Можно ли продлить заказ или вернуть самокат раньше?" должен получить ответ "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."')


    def testDropDownListQuestion5(self,driver):
        main_page = MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickAccordiodionButton05()
        text=main_page.ShowTextAccordioPanel05()
        return text
        assert text=="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    @allure.title('Проверка на "https://qa-scooter.praktikum-services.ru/"Выпадающий список в разделе «Вопросы о важном»')  # декораторы
    @allure.description('На вопрос"Вы привозите зарядку вместе с самокатом?" должен получить ответ "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."')


    def testDropDownListQuestion6(self,driver):
        main_page = MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickAccordiodionButton06()
        text=main_page.ShowTextAccordioPanel06()
        return text
        assert text=="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.title('Проверка на "https://qa-scooter.praktikum-services.ru/" Выпадающий список в разделе «Вопросы о важном»')  # декораторы
    @allure.description('На вопрос"Можно ли отменить заказ?" должен получить ответ "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."')

    def testDropDownListQuestion7(self,driver):
        main_page = MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickAccordiodionButton07()
        text=main_page.ShowTextAccordioPanel07()
        return text
        assert text=="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title('Проверка на "https://qa-scooter.praktikum-services.ru/" Выпадающий список в разделе «Вопросы о важном»')  # декораторы
    @allure.description('На вопрос"Я жизу за МКАДом, привезёте?" должен получить ответ "Да, обязательно. Всем самокатов! И Москве, и Московской области."')

    def testDropDownListQuestion8(self,driver):
        main_page = MainPage(driver)
        main_page.ClickCoockieConfirmButton()
        main_page.ClickAccordiodionButton08()
        text=main_page.ShowTextAccordioPanel08()
        return text
        assert text=="Да, обязательно. Всем самокатов! И Москве, и Московской области."
