import requests
import urllib.request

resposta = requests.get('https://pokeapi.co/api/v2/pokemon/bulbasaur')

if resposta.status_code == 200:
    dados = resposta.json()

