from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
import urllib.request
from time import sleep
import requests
import json
from rembg import remove

# definindo as cores da pokedex

vermelho = '#c73736'
vermelho_escuro = '#8b2823'
cinza_claro = '#e8ddc1'
cor_botao = '#3f3c4d'
azul_claro = '#5898b1'


# DEFININDO TAMANHO DA JANELA
# A PARTE SUPERIOR DA POKEDEX SERÁ 17% O VALOR TOTAL
# A PARTE INFERIOR SERÁ 12%
# O MEIO SERÁ O RESTANTE
x = '400'
y = '660'
size = x + 'x' + y
janela = Tk()
janela.title("Pykedex by GreenShimada")
janela.geometry(size)
janela.configure(background=vermelho_escuro)
janela.resizable(width=FALSE,height=FALSE)

# seções (frames)
frameCima = Frame(janela, width=int(x), height=(int(y)*0.17), bg=vermelho, relief='raised', borderwidth=3)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=int(x), height=(int(y)*0.71), bg=vermelho_escuro, relief='flat')
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=int(x), height=(int(y)*0.12), bg=vermelho, relief='raised', borderwidth=2)
frameBaixo.grid(row=2, column=0)

visor = Image.open('pokeW.jpg')
visor = visor.resize((400, 397))
visor = ImageTk.PhotoImage(visor)
teste = Label(frameMeio, image=visor)
teste.place(y=0, x=0)

def tirarFundoPNG(caminho, saida):
    input = Image.open(caminho)
    output = remove(input) #amo python
    output.save(saida)

def procurar():
    global poke_img
    # Obtendo a palavra
    palavra = e_palavra.get()
    print(palavra)
    api_link = f'https://pokeapi.co/api/v2/pokemon/{palavra}'
    r = requests.get(api_link)
    dados = json.loads(r.text)

    # imagem
    img = dados['sprites']['front_default']
    poke_img = urllib.request.urlretrieve(img, 'poke.png')
    tirarFundoPNG('poke.png','poke.png')
    poke_img = Image.open(poke_img[0])
    poke_img = poke_img.resize((300, 300))
    poke_img = ImageTk.PhotoImage(poke_img)
    poke_img_ready = Label(frameMeio, image=poke_img, width=299, height=299, bg='#ffffff')
    poke_img_ready.place(x=(int(x)/2 - 150), y=20)

    abilities = []
    for ability in dados['abilities']:
        abilities.append(ability['ability']['name'])
    habilidades = ("Habilidades:", ", ".join(abilities))
    tk_hab = Label(frameMeio, text=habilidades, font='Ivy 9', bg='#ffffff')
    tk_hab.place(x=30, y=300)

# Personalizando Frame do Meio

l_palavra = Label(frameCima, text='Digite o nome de um pokemon', height=1, anchor=NW, font='Ivy 11', bg=vermelho, fg=cinza_claro)
l_palavra.place(x=7, y=15)
e_palavra = Entry(frameCima, width=18, font=('Ivy 14 '), justify='center',relief="solid")
e_palavra.place(x=10, y=41)

b_procurar = Button(frameCima,command=procurar, compound=CENTER,width=10, text='Procurar' ,bg=azul_claro,font=('Ivy 11'), overrelief=RIDGE,)
b_procurar.place(x=260, y=40)




janela.mainloop()