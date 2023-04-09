from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
import urllib.request
from time import sleep
import requests
import json

# definindo as cores da pokedex

vermelho = '#c73736'
vermelho_escuro = '#8b2823'
cinza_claro = '#e8ddc1'
cor_botao = '#3f3c4d'
azul_claro = '#5898b1'
co1 = "#feffff"  # branca
co4 = "#403d3d"   # letra

janela = Tk()
janela.title("Pykedex by GreenShimada")
janela.geometry('380x415')
janela.configure(background=vermelho_escuro)
janela.resizable(width=FALSE,height=FALSE)

# seções (frames)
frameCima = Frame(janela, width=380, height=70, bg=vermelho, relief='flat', borderwidth=3)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=380, height=295, bg=vermelho_escuro, relief='flat')
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=380, height=50, bg=vermelho, relief='raised', borderwidth=2)
frameBaixo.grid(row=2, column=0)



def procurar():
    global app_img
    # Obtendo a palavra
    palavra = e_palavra.get()
    print(palavra)
    api_link = f'https://pokeapi.co/api/v2/pokemon/{palavra}'
    r = requests.get(api_link)
    dados = json.loads(r.text)

    abilities = []
    for ability in dados['abilities']:
        abilities.append(ability['ability']['name'])
    habilidades = ("Habilidades:", ", ".join(abilities))
    tk_hab = Label(frameMeio, text=habilidades, font='Ivy 9')
    tk_hab.place(x=50, y=90)

    # imagem
    img = dados['sprites']['front_default']
    app_img = urllib.request.urlretrieve(img,'poke.png')
    app_img = Image.open(app_img[0])
    app_img = app_img.resize((40, 40))
    app_img = ImageTk.PhotoImage(app_img)
    app_logo = Label(frameMeio, image=app_img, width=100, height=100, )
    app_logo.place(x=50, y=150)

# Personalizando Frame do Meio

l_palavra = Label(frameMeio, text='Digite o nome de um pokemon', height=1, anchor=NW, font='Ivy 10', bg=azul_claro, fg=cinza_claro)
l_palavra.place(x=7, y=15)
e_palavra = Entry(frameMeio, width=18, font=('Ivy 14 '), justify='center',relief="solid")
e_palavra.place(x=10, y=41)

b_procurar = Button(frameMeio,command=procurar, compound=LEFT,width=100, text='  Procurar' ,bg=vermelho, fg=azul_claro,font=('Ivy 11'), overrelief=RIDGE)
b_procurar.place(x=230, y=40)




janela.mainloop()