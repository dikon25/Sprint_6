from faker import Faker
import random


class RegData:
    def reg_up_data_name():
        fake=Faker('RU')
        name = fake.first_name()
        return name
    def reg_up_data_surname():
        fake = Faker('RU')
        surname = fake.last_name()
        return surname
    def reg_up_data_phone():
        fake = Faker('RU')
        phone = fake.msisdn()
        return phone
    def reg_up_data_address():
        fake=Faker('RU')
        address = fake.administrative_unit()
        return address
    def reg_up_data_comment():
        fake = Faker('RU')
        comment = "Для" + fake.name()
        return comment
    def reg_up_data_metro():
        fake = Faker('RU')
        number_metro_station = random.randint(1, 30)
        return number_metro_station
    def reg_up_data_date():
        fake=Faker('RU')
        date = fake.date()
        return date

class QuestionsAnswers:
        assert_answer = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                         'Да, обязательно. Всем самокатов! И Москве, и Московской области.']

