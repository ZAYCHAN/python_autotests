#- Проверь, что ответ запрос **GET /trainers** приходит с кодом 200

#Проверь, что в ответе приходит строчка с именем твоего тренера
#(Не забудь прописать в квери id твоего тренера (​​​​trainer_id​​​​))

import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '96a927dc511b8fe520383c591ea3f693'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '33120'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_body_response():
    response_trainer_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainer_name.json()["data"][0]["trainer_name"] == 'Shredder'