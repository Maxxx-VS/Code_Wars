import json
class User:
    def __init__(self, name_user, email_user, password_user):
        self.name_user = name_user
        self.email_user = email_user
        self.password_user = password_user
    def add_json(self):
        global data
        print("ТРЕБУЕТСЯ РЕГИСТРАЦИЯ!", "\n")
        self.name_user = input("Введите своё имя: ")
        self.email_user = input("Введите свою почту: ")
        self.password_user = input("Создайте пароль : ")
        data = {'name': self.name_user, 'email': self.email_user, 'password': self.password_user}
        with open('data_file.json', 'a', encoding='utf-8') as file:
            json.dump(data, file)
            file.write("\n")
        print("ВЫ ЗАРЕГИСТРИРОВАЛИСЬ!!!", "\n")
        question_change = input(f"Хотите сменить пароль??? (да/нет): ")
        if question_change == "да" or question_change == "yes" or question_change == "y":
            Change().change_password(self.password_user)
        else:
            pass


class Change:
    def change_password(self, password_user):
        global file
        self.password_user = password_user
        print(f'Ваш текущий пароль: {self.password_user}')
        print(data['password'])
        data['password'] = 1
        print(data['password'])




        # change_password = input("Введите новый пароль: ")
        # data =
        # data.update('password', change_password)

        # with open('data_file.json', 'a') as file:
        #     json.dump(data, file)
        #     file.write("\n")











User("name_user", 'email_user', "password_use").add_json()


