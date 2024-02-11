import json

class User:
    def __init__(self, name_user, email_user, password_user):
        self.name_user = name_user
        self.email_user = email_user
        self.password_user = password_user
    def add_json(self):
        global data
        print(f"ДЛЯ ДАЛЬНЕЙШЕЙ РАБОТЫ" , "\n"
              f"ТРЕБУЕТСЯ РЕГИСТРАЦИЯ", "\n")
        self.name_user = input("Введите своё имя: ")
        self.email_user = input("Введите свою почту: ")
        self.password_user = input("Создайте пароль : ")
        data = [{'name': self.name_user, 'email': self.email_user, 'password': self.password_user}]
        with open('data_file.json', 'a', encoding='utf-8') as file:
            json.dump(data, file)
            file.write("\n")
        print("ВЫ ЗАРЕГИСТРИРОВАЛИСЬ!", "\n")
        question_change = input(f"Хотите сменить пароль??? (да/нет): ")
        print("\n")
        if question_change == "да" or question_change == "yes" or question_change == "y" or question_change == "+":
            Change().change_password(self.password_user)
        else:
            Authentication().authentication_user(self.name_user, self.password_user)


class Change:
    def change_password(self, password_user):
        self.password_user = password_user
        print(f'Ваш текущий пароль: {self.password_user}')
        change_password = input("Введите новый пароль: ")


        # json_data = json.loads(data)
        # more_json_string = '{"name": "---", "email": "---", "password": "---"}'
        # more_json_data = json.loads(more_json_string)
        # json_data.update(more_json_data)


        # json_data = json.loads(data)
        # json_data[0]['name'] = 2023


        # with open("data_file.json", "r+") as f:
        #     d = json.load(f)
        #     d.write({
        #         "name": 4,
        #         "email": "Rahul Shinde",
        #         "password": "rahul@gmail.com"})













class Authentication:
    def authentication_user(self, name_user, password_user):
        self.name_user = name_user
        self.password_user = password_user
        print(f"ДОБРО ПОЖАЛОВАТЬ, {self.name_user}! ДЛЯ ДАЛЬНЕЙШЕЙ РАБОТЫ"
              f"ПРОДТВЕРДИ СВОИ ДАННЫЕ: ")
        auth_name = input("ВВЕДИ ИМЯ: ")
        auth_password = input("ВВЕДИ ПАРОЛЬ: ")
        if auth_name == data['name'] and auth_password == ['password']:
            print("yes")

















User("name_user", 'email_user', "password_use").add_json()


