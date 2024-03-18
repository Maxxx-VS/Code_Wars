from gpt import GPT


# Объект GPT
gpt = GPT(system_content="Ты - дружелюбный помощник для решения задач по математике. Давай подробный ответ с решением на русском языке")


# Диалог с GPT
def gpt_dialog():
    print('Можешь ввести любую задачу, и я постараюсь её решить')
    print('-Если напишешь "продолжи", я продолжу объяснять задачу')
    print('-Для завершения диалога напиши "конец"')
    while True:
        # Получение запроса от пользователя
        user_request = input("Ввод: ")

        # заканчиваем работу с GPT
        if user_request.lower() == 'конец':
            break

        # Проверка запроса на количество токенов
        request_tokens = gpt.count_tokens(user_request)
        while request_tokens > gpt.MAX_TOKENS:
            user_request = input("Запрос несоответствует кол-ву токенов\nИсправьте запрос: ")
            request_tokens = gpt.count_tokens(user_request)

        # Не продолжаем ответ
        if user_request.lower() != 'продолжи':
            gpt.clear_history()

        # Формирование промта
        json = gpt.make_promt(user_request)

        # Отправка запроса
        resp = gpt.send_request(json)

        # Проверяем ответ на наличие ошибок и парсим его
        response = gpt.process_resp(resp)
        if not response[0]:
            print("Не удалось выполнить запрос...")
        # Выводим ответ или сообщение об ошибке
        print(response[1])


# Выход =)
def end():
    print("До новых встреч!")
    exit(0)


def start():
    menu = {
        "1": {
            "text": "Общение с GPT",
            "func": gpt_dialog
        },
        "2": {
            "text": "Выход",
            "func": end
        }
    }

    print("Добро пожаловать в Чат-с-GPT\nЯ твой помощник для решения задач по математике")
    # Бесконечный цикл
    while True:
        # Вывод меню
        print("Меню:")
        for num, item in menu.items():
            print(f"{num}. {item['text']}")

        # Получение корректного выбора пользователя
        choice = input("Выбери: ")
        while choice not in menu:
            choice = input("Выбери корректный пункт: ")

        # Вызов функции из меню
        menu[choice]['func']()


if __name__ == "__main__":
    start()