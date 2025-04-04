import requests

def extrair_medalhas_pais(nome_pais):
    url = f"https://apis.codante.io/olympic-games/countries/{nome_pais}"
    response = requests.get(url)
    pais = response.json()
    return {
        "total": pais["total_medals"],
        "ouro": pais["gold_medals"],
        "prata": pais["silver_medals"],
        "bronze": pais["bronze_medals"]
    }

nome_pais = "brasil"
medalhas = extrair_medalhas_pais(nome_pais)
print("Informações de medalhas do país:")
print(f"Total: {medalhas['total']}")
print(f"Ouro: {medalhas['ouro']}")
print(f"Prata: {medalhas['prata']}")
print(f"Bronze: {medalhas['bronze']}")