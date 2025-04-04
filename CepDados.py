import requests 

def dados(cep):
    url = f"https://viacep.com.br/ws/09195000/json/"    
    txt = requests.get(url)
    a = txt.json()
    return a

print(dados("09195000")) 