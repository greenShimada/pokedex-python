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
        x = '800'
        y = '550'

        # FRAME DE CIMA (PARTE SUPERIOR DA POKEDEX ONDE TEM O INPUT)
        frameCima = Frame(janela, width=int(x), height=82, bg=vermelho, relief='raised', borderwidth=3)
        frameCima.grid(row=0, column=0, columnspan=2)

        # FRAME DO MEIO (CORPO DA POKEDEX ONDE MOSTRA O POKEMON)
        self.frameEsquerda = Frame(janela, width=400, height=468, bg=vermelho_escuro, relief='flat')
        self.frameEsquerda.grid(row=1, column=0)

        self.frameDireita = Frame(janela, width=400, height=468, bg=vermelho_escuro, relief='flat')
        self.frameDireita.grid(row=1, column=1)

        global visor
        global visor2


        self.bg = './bg/newAir.jpg'

        visor2 = Image.open(self.bg)
        visor2 = ImageTk.PhotoImage(visor2)
        self.visorobj2 = Label(self.frameDireita, image=visor2, borderwidth=-1)
        self.visorobj2.place(y=0, x=-400)

        visor = Image.open(self.bg)
        visor = ImageTk.PhotoImage(visor)
        self.visorobj = Label(self.frameEsquerda, image=visor, borderwidth=-1)
        self.visorobj.place(y=0, x=0)


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

        self.labelNome = Label(self.frameDireita,height=1, anchor=NW, font='Ivy 16')
        self.labelHabilidade = Label(self.frameDireita, anchor=NW, font='Ivy 16')


class Pokemon():
        def __init__(self, nome, tipos, habilidades, url_gif):
            self.nome = nome
            self.tipos = tipos
            self.habilidades = habilidades
            self.url_gif = url_gif



