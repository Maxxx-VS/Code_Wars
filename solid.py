### Single Responsibility Principle
class FileManager: # Он делает то, что нужно, без лишнего функционала
    def read_file(self, file_path):
        # код для чтения файла
    def wright_file(self,file_path, data):
        # код для записи файла



### Open‐Closed Principle
class PaymentProcessor: # PaymentProcessor зависит от PaymentProvidr что позволяет добавлять новых провайдеров не изменяя код PaymentProcessor.
    def process_payment(self, payment_providr, amount):
        payment_providr.process_payment(amount)

class PaymentProvidr:
    def process_payment(self, amount):
        pass

class MirPaymentProvidef(PaymentProvidr):
    def process_payment(self, amount):
        # код для обработки платежа через Мир

class PayPalPaymentProvidef(PaymentProvidr):
    def process_payment(self, amount):
        # код для обработки платежа через PayPal


### Liskov Substitution Principle
class Rectangle: # класс Squre является подтипом Rectangle, но все методы одни и те же и работают подобно, заменяют другдруга
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height

    def get_area(self):
        print(self.height * self.widht)

class Squre(Rectangle):
    def __init__(self, side_lenght):
        self.side_lenght = side_lenght
        super().__init__(side_lenght, side_lenght)

    def set_side_lenght(self, side_lenght):
        self.side_lenght = side_lenght
        self.widht = side_lenght
        self.height = side_lenght

Rectangle(10, 10).get_area()
a = Rectangle(10, 20).get_area()

Squre(30).get_area()
b = Squre(40).get_area()


### Interface Segregation Principle
class Printer:
    def print(self, document):
        pass
class Scaner:
    def scan(self, document):
        pass
class Fax:
    def fax(self, document):
        pass

class Product(Printer, Scaner, Fax):
    def print(self, document):
        pass
    def scan(self, document):
        pass
    def fax(self, document):
        pass

### Dependency Inversion Principle
class Database_Connector: # класс UserServis зависти от Database_Connector но не зависит от конкретной реализации. Подключение к БД не изменяя код UserServis
    def connect(self):
        # connect to DB
        pass
class UserServis:
    def __init__(self, database_connector):
        self.database_connector =  database_connector
    def get_user(self, user_id):
        connection = self.database_connector.connect()
        # получение пользователя из БД


aa = lambda x: x*2
print(aa(5))