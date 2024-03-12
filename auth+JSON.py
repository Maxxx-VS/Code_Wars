import json
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def change_password(self, new_password):
        self.password = new_password
class UserRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_users()
    def load_users(self):
        try:
            with open(self.file_path) as f:
                return json.load(f)
        except FileNotFoundError:
            return "Error"

    def save_user(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.users, f)

 # доработать сохр

    def create_user(self, user):
        self.users[user.email] = {
            'name': user.name,
            'password': user.password,
        }
        self.save_user()

    def get_user_by_email(self, email):
        if email in self.users:
            data = self.users[email]
            return User(data['name'], email, data['password'])
        return None

class AuthenticationService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def sign_up(self, name, email, password):
        user = User(name, email, password)
        self.user_repository.create_user(user)

    def sign_in(self, email, password):
        user = self.user_repository.get_user_by_email(email)

        if user and user.password == password:
            return True
        else:
            return False

user_repository = UserRepository('users.json')
auth_servise = AuthenticationService(user_repository)
auth_servise.sign_up("John-1", "jjj@ya.ru", '12345')
auth_servise.sign_up("Olga", "ooo@ya.ru", '---')

email = input('Введи почту: ')
password = input('Введи пароль: ')
sign_in = auth_servise.sign_in(email, password)
if sign_in:
    print("OK")
else:
    print("NO")