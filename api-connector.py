import requests
import json

# Fazendo uma solicitação HTTP para obter a lista de todos os Pokémon
url = 'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0'
response = requests.get(url)

# Carregando os dados JSON da resposta
data = json.loads(response.text)

nomeProcurado = str(input('Digite um pokemon: '))

# Iterando sobre os resultados e extraindo o nome e as habilidades de cada pokémon
for pokemon in data['results']:
    if pokemon['name'] == nomeProcurado:
        name = str(pokemon['name'])
        print("Nome:", name.title())
        # Fazendo uma solicitação HTTP para obter mais informações sobre o pokémon
        pokemon_url = pokemon['url']
        pokemon_response = requests.get(pokemon_url)
        pokemon_data = json.loads(pokemon_response.text)

        # Extraindo as habilidades do pokémon
        abilities = []

        for ability in pokemon_data['abilities']:
            abilities.append(ability['ability']['name'])

        print("Habilidades:", ", ".join(abilities))
        print()


