from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk

class Pokedex():
    def __init__(self, janela):


        # definindo as cores da pokedex
        vermelho = '#c73736'
        vermelho_escuro = '#8b2823'
        cinza_claro = '#e8ddc1'
        cor_botao = '#3f3c4d'
        azul_claro = '#5898b1'
        x = '400'
        y = '660'

        # FRAME DE CIMA (PARTE SUPERIOR DA POKEDEX ONDE TEM O INPUT)
        frameCima = Frame(janela, width=int(x), height=(int(y) * 0.17), bg=vermelho, relief='raised', borderwidth=3)
        frameCima.grid(row=0, column=0)
        # FRAME DO MEIO (CORPO DA POKEDEX ONDE MOSTRA O POKEMON)
        self.frameMeio = Frame(janela, width=int(x), height=(int(y) * 0.71), bg=vermelho_escuro, relief='flat')
        self.frameMeio.grid(row=1, column=0)
        # FRAME DE BAIXO (PARTE INFERIOR DA POKEDEX ONDE NÃO TEM NADA)
        frameBaixo = Frame(janela, width=int(x), height=(int(y) * 0.12), bg=vermelho, relief='raised', borderwidth=2)
        frameBaixo.grid(row=2, column=0)

        global visor
        visor = Image.open('visorresized.jpg')
        #visor = visor.resize((400, 397))
        visor = ImageTk.PhotoImage(visor)
        teste = Label(self.frameMeio, image=visor)
        teste.place(y=0, x=0)

        # CRIANDO A LABEL COM O TEXTO
        l_palavra = Label(frameCima, text='Digite o nome de um pokemon', height=1, anchor=NW, font='Ivy 11',
                          bg=vermelho, fg=cinza_claro)
        l_palavra.place(x=7, y=15)

        # CRIANDO  O INPUT PARA DIGITAR O NOME DO POKEMON
        self.e_palavra = Entry(frameCima, width=18, font=('Ivy 14 '), justify='center', relief="solid")
        self.e_palavra.place(x=10, y=41)
        self.botao_procurar = Button(frameCima, compound=CENTER, width=10,
                            text='Procurar', bg=cor_botao,
                            font=('Ivy 11'), overrelief=RIDGE)
        self.botao_procurar.place(x=260, y=40)
#class Botao_pesquisa():
   # def __init__(self, janela):






class Pokemon():
    def __init__(self, nome, tipos, habilidades, url_gif):
        self.nome = nome
        self.tipos = tipos
        self.habilidades = habilidades
        self.url_gif = url_gif

    def exibir_pokemon(self):
        print(f'Nome: {self.nome.title()},\n'
              f'Tipos = {self.tipos},\n'
              f'Habilidades = {self.habilidades},\n'
              f'Url_gif = {self.url_gif}')


    pass
