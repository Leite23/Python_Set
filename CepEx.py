import requests

def extrair_informacoes_cep(cep):

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    return response.json()

cep = "09195000"
informacoes = extrair_informacoes_cep(cep)

if informacoes:
    print("Informações do endereço:")
    print(f"Logradouro: {informacoes['logradouro']}")
    print(f"Bairro: {informacoes['bairro']}")
    print(f"Cidade: {informacoes['localidade']}")
    print(f"Estado: {informacoes['uf']}")
else:
    print("CEP não encontrado.")