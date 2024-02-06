import json
class User:
    def __init__(self, name_user, email_user, password_user):
        self.name_user = name_user
        self.email_user = email_user
        self.password_user = password_user
    def add_json(self):
        data = {'name': self.name_user, 'email': self.email_user, 'password': self.password_user}
        with open('data_file.json', 'a') as file:
            json.dump(data, file)

User('max', 'fff@ya.ru', "123").add_json()


