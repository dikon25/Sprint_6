from faker import Faker
import random
import sys
class Url:
    url_main="https://qa-scooter.praktikum-services.ru/"
    url_order="https://qa-scooter.praktikum-services.ru/order"
    url_dzen="https://dzen.ru/?yredirect=true"
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
    def PrintPath():
        print(sys.argv[0])

data=RegData
data.PrintPath()


