from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk, ImageSequence
import urllib.request
import requests
import json
import math


class Pesquisador_Pokemon():
    def __init__(self, nome_pokemon):
        self.nome = nome_pokemon.lower()


    def retorna_gif_sem_fundo(self):
        lista_pokemon = list()
        gif_novo = list()
        gif_path = './img/poke.gif'
        gif = Image.open(gif_path)
        largura_or, altura_or = gif.size
        largura = largura_or * 3
        altura = altura_or * 3

        fundo = Image.open('./bg/visorTerra.png')
        crop = [
            math.floor(200 - (largura / 2)),
            20,
            math.floor(200 + (largura / 2)) ,
            20 + altura
        ]
        fundo = fundo.crop((
            crop[0],
            crop[1],
            crop[2],
            crop[3]

        ))
        fundo = fundo.convert("RGBA")
        print(fundo.size)


        for frame in range(gif.n_frames):
            gif.seek(frame)
            atual = gif.copy()
            atual = atual.convert("RGBA")
            atual = atual.resize((
                largura,
                altura
            ))


            imagem_final = Image.alpha_composite(fundo, atual)
            lista_pokemon.append(imagem_final)

        for imagem in lista_pokemon:
            gif_novo.append(imagem.copy())

        gif_novo[0].save("./img/poke.gif", format="GIF", save_all=True, append_images=gif_novo,
                 duration=50, loop=0)



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



