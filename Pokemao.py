import requests

def extrair_informacoes_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}/"
    response = requests.get(url)
    pokemon = response.json()
    return {"tipo": pokemon["types"][0]["type"]["name"], "id": pokemon["id"]}

nome_pokemon = "pikachu"
informacoes = extrair_informacoes_pokemon(nome_pokemon)
print("Informações do Pokémon:")
print(f"Tipo: {informacoes['tipo']}")
print(f"ID: {informacoes['id']}")