import json
class User:
    def __init__(self, name_user, email_user, password_user):
        self.name_user = name_user
        self.email_user = email_user
        self.password_user = password_user
    def add_json(self):
        print("ТРЕБУЕТСЯ РЕГИСТРАЦИЯ!", "\n")
        self.name_user = input("Введите своё имя: ")
        self.email_user = input("Введите свою почту: ")
        self.password_user = input("Создайте пароль : ")
        data = {'name': self.name_user, 'email': self.email_user, 'password': self.password_user}
        with open('data_file.json', 'a') as file:
            json.dump(data, file)
            file.write("\n")
        print("ВЫ ЗАРЕГИСТРИРОВАЛИСЬ!!!", "\n")
        c = input(f"Хотите сменить пароль??? (да/нет): ")
        if c == "да":
            Change().change_password(self.password_user)
        else:
            print("дем дальше")



class Change:
    def change_password(self, password_user):
        self.password_user = password_user
        print(f'Ваш текущий пароль: {self.password_user}')
        self.password_user = input("Введите новый пароль: ")
        # перезаписываем JSON











User("name_user", 'email_user', "password_use").add_json()


