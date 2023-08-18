import requests
token='ca2b8b647c2a3f1a74f0876fa7e35154'
host='https://api.pokemonbattle.me:9104' 

'''responce_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Mouse",
    "photo": "https://dolnikov.ru/pokemons/albums/183.png"
},
headers= {'Content-Type':'application/json', 
          'trainer_token':token})

print(responce_add_pokemon.text)'''

responce_change_name_pokemon=requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6240",
    "name": "Funny",
    "photo": "https://dolnikov.ru/pokemons/albums/107.png"
},
headers= {'Content-Type':'application/json', 
          'trainer_token':token})

print(responce_change_name_pokemon.text)

responce_catch_pokemon=requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6240"
},
headers= {'Content-Type':'application/json', 
          'trainer_token':token})

print(responce_catch_pokemon.text)
