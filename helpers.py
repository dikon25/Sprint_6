from faker import Faker
import random

class RegData:
    def Reg_up_data_name():
        fake=Faker('RU')
        name = fake.first_name()
        return name
    def Reg_up_data_surname():
        fake = Faker('RU')
        surname = fake.last_name()
        return surname
    def Reg_up_data_phone():
        fake = Faker('RU')
        phone = fake.msisdn()
        return phone
    def Reg_up_data_address():
        fake=Faker('RU')
        address = fake.administrative_unit()
        return address
    def Reg_up_data_comment():
        fake = Faker('RU')
        comment = "Для" + fake.name()
        return comment
    def Reg_up_data_metro():
        fake = Faker('RU')
        number_metro_station = random.randint(1, 30)
        return number_metro_station
    def Reg_up_data_date():
        fake=Faker('RU')
        date = fake.date()
        return date

class QuestionsAnswers:
        def answer_1(self):
            answer_1= 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
            return answer_1

        def answer_2(self):
            self.answer='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
            return answer
        def answer_3(self):
            self.answer='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
            return answer
        def answer_4(self):
            self.answer='Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
            return answer
        def answer_5(self):
            self.answer='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
            return answer
        def answer_6(self):
            self.answer='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
            return answer
        def answer_7(self):
            self.answer='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
            return answer
        def answer_8(self):
            self.answer='Да, обязательно. Всем самокатов! И Москве, и Московской области.'
            return answer



