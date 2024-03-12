import requests
from bs4 import BeautifulSoup
import json


BASE_DOMAIN = 'https://images.nasa.gov'

q = 'Apollo'


def nasa():
    API = 'YB6sFSMjkOse6CCulktxKE0G64JNTPdkhKyFKdpU'
    url = 'https://images.nasa.gov/images/'
    param = {
        "API-KEY" : API
    }
    response = requests.get(url, param).json()


    print(response)


