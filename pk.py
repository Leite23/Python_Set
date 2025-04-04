import requests

def pokemon(nome):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
    a = request.get(url)
    info = a.json()
    id = info['id']
    tipo = info['types'][0]['type']['name']
    return id, tipo

print(dados_pokemon('pikachu'))