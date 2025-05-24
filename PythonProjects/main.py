import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '96a927dc511b8fe520383c591ea3f693'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

change_pokemon_name = {
    "pokemon_id": "324312",
    "name": "Unicron",
    "photo_id": 10
}

catch_pokemon = {
    "pokemon_id": "324312"
}

#Создание покемона

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.text)

#Смена имени покемона

response_change_pokemon_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_pokemon_name)
print(response_change_pokemon_name.text)

#Поймать покемона в покебол

response_catch_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_pokemon)
print(response_catch_pokemon.text)


