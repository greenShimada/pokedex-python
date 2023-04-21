from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
import urllib.request
import requests
import json



class Pesquisador_Pokemon():
    def __init__(self, nome_pokemon):
        self.nome = nome_pokemon.lower()

    def pegar_url(self, nome_pokemon):
        url = f'https://pokeapi.co/api/v2/pokemon/{nome_pokemon}'
        return url

    def retornar_resposta(self, url):
        self.resposta = requests.get(url)
        if self.resposta.status_code != 200:
            self.resposta = requests.get('https://pokeapi.co/api/v2/pokemon/mewtwo')
            return self.resposta
        else:
            return self.resposta

    def retorna_json(self, resposta):
        dados = json.loads(resposta.text)
        return dados

    def retorna_link_gif(self, json):
        return json['sprites']['versions']['generation-v']['black-white']['animated']['front_default']

    def retorna_habilidades(self, json):
        habilidades = [habilidade["ability"]["name"].capitalize() for habilidade in json["abilities"]]
        return habilidades

    def retorna_tipos(self, json):
        tipos = [tipo["type"]["name"].capitalize() for tipo in json["types"]]
        return tipos


    def retorna_gif(self, url_gif):
        return urllib.request.urlretrieve(url_gif, './img/poke.gif')

    def abre_gif(self, gif):
        return Image.open(gif)

    def retorna_frames(self, obj_imagem):
        return obj_imagem.n_frames

    def retorna_nome(self, json):
        nome = json['name']
        return nome



