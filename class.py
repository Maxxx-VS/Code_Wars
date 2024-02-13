import json

def add_user():
    username = input("Введите логин пользователя: ")
    password = input("Введите пароль пользователя: ")


    with open('users.json', 'r') as file:
        data = json.load(file)

    data[username] = password

    with open('users.json', 'w') as file:
        json.dump(data, file)

    print("Пользователь успешно добавлен!")

def change_password():
    username = input("Введите логин пользователя, пароль которого вы хотите изменить: ")
    new_password = input("Введите новый пароль: ")

    with open('users.json', 'r') as file:
        data = json.load(file)

    if username in data:
        data[username] = new_password

        with open('users.json', 'w') as file:
            json.dump(data, file)

        print("Пароль успешно изменен!")
    else:
        print("Пользователь не найден!")

while True:
    choice = input("Выберите действие (1 - добавить пользователя, 2 - изменить пароль, 0 - выход): ")

    if choice == "1":
        add_user()
    elif choice == "2":
        change_password()
    elif choice == "0":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")