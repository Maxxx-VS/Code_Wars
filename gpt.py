import requests
from transformers import AutoTokenizer

class GPT:
    def __init__(self, system_content="Представь, что ты дружелюбный помощник по математике. Давай подробный ответ с решением на русском языке"):
        self.system_content = system_content
        self.URl = 'http://localhost:1234/v1/chat/completions'
        self.HEADERS = {"Content-Type": "application/json"}
        self.MAX_TOKENS = 150
        self.assistant_content = "Решим задачу по шагам"

        # Подсчитываем кол-во токенов в промте
    @staticmethod
    def count_tokens(promt):
        tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")  # название модели
        return len(tokenizer.encode(promt))

    def process_resp(self, response) -> [bool, str]:
        # Проверка статуса кода
        if response.status_code < 200 or response.status_code >= 300:
            self.clear_history()
            return False, f"Ошибка: {response.status_code}"

        # Проверка JSON
        try:
            full_response = response.json()
        except:
            self.clear_history()
            return False, f"Ошибка получения JSON"

        # Проверка сообщения об ошибке
        if "error" in full_response or "choices" not in full_response:
            self.clear_history()
            return False, f"Ошибка: {full_response}"

        # Результат
        result = full_response['choices'][0]['message']['content']

        # Пустой результат = объяснение закончено
        if result == "":
            self.clear_history()
            return True, self.assistant_content

    # Формирование промта
    def make_promt(self, user_request):
        if user_request == "":
            user_request = "продолжи"
        json = {
            "messages": [
                {'role': 'system', 'content': self.system_content}, # Говорит модели ГПТ её роль
                {'role': 'user', 'content': user_request},
                {'role': 'assistant', 'content': self.assistant_content} # Отвечает с поправкой на историю ответа (ссылка на предыдущий ответ)
            ],
            "temperature": 0.8, # Вариация токенов для ответа
            "max_tokens": self.MAX_TOKENS,
        }
        return json

    # Отправка запроса
    def send_request(self, json):
        resp = requests.post(url=self.URl, headers=self.HEADERS, json=json)
        return resp

    # Сохраняем история общения
    def save_history(self, content_response):
        self.assistant_content += content_response

    # Очистка истории общения
    def clear_history(self):
        self.assistant_content = "Решим задачу по шагам"

