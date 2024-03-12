import requests
from bs4 import BeautifulSoup
from sdamgia import SdamGIA
import random

BASE_DOMAIN = 'sdamgia.ru'
SUBJECT_BASE_URL = {
    'math': f'https://math-ege.{BASE_DOMAIN}',
    'phys': f'https://phys-ege.{BASE_DOMAIN}',
    'mathb': f'https://mathb-ege.{BASE_DOMAIN}',
    'inf': f'https://inf-ege.{BASE_DOMAIN}',
}

def fnd_task(subject, word, page):
    # url = SUBJECT_BASE_URL[subject]
    url = f'{SUBJECT_BASE_URL[subject]}/search?search={word}&page{page}'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    task = [i.text.split()[-1] for i in soup.find_all('span', {'class': 'prob_nums'})]
    return task

print(fnd_task('math', 'площадь', '30'))



from sdamgia import SdamGIA

sdamgia = SdamGIA()

subject = 'math'
id = '1001'
sdamgia.get_problem_by_id(subject, id)