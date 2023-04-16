from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
import urllib.request
import requests
import json


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

# FRAME DE CIMA (PARTE SUPERIOR DA POKEDEX ONDE TEM O INPUT)
frameCima = Frame(janela, width=int(x), height=(int(y)*0.17), bg=vermelho, relief='raised', borderwidth=3)
frameCima.grid(row=0, column=0)
# FRAME DO MEIO (CORPO DA POKEDEX ONDE MOSTRA O POKEMON)
frameMeio = Frame(janela, width=int(x), height=(int(y)*0.71), bg=vermelho_escuro, relief='flat')
frameMeio.grid(row=1, column=0)
# FRAME DE BAIXO (PARTE INFERIOR DA POKEDEX ONDE NÃO TEM NADA)
frameBaixo = Frame(janela, width=int(x), height=(int(y)*0.12), bg=vermelho, relief='raised', borderwidth=2)
frameBaixo.grid(row=2, column=0)

# POSICIONANDO O "MONITOR" DA POKEDEX
visor = Image.open('pokeW.jpg')
visor = visor.resize((400, 397))
visor.save('visorresized.jpg')
visor = ImageTk.PhotoImage(visor)
teste = Label(frameMeio, image=visor)
teste.place(y=0, x=0)


def diminuirImagem(img):
    with Image.open(img) as pokemon:
        img_pretobranco = pokemon.convert('L')            # Converte a imagem para escalas de cinza
        bbox = img_pretobranco.getbbox()                  # Acha sozinho o menor tamanho possível sem o fundo (amo python)
        pokemon = pokemon.crop(bbox)                      # bbox retorna uma tupla com as coordenadas da borda superior esquerda e inferior direita, logo ele sozinho serve de parametro para o crop
        pokemon.save(img, format='PNG')                   # salva a imagem com o tamanho nova por cima da antiga

def procurar():
    global poke_img                                                 # SE NÃO FOR GLOBAL, A IMAGEM NÃO É RECONHECIDA APÓS O FIM DA FUNÇÃO
    palavra = e_palavra.get()                                       # RECEBE O QUE FOI DIGITADO NO INPUT
    palavra = palavra.lower()                                       # PADRONIZA NO MINUSCULO
    api_link = f'https://pokeapi.co/api/v2/pokemon/{palavra}'       # ACESSA A API COM O NOME DO POKEMON DIGITADO
    r = requests.get(api_link)
    if r.status_code != 200:
        api_link = f'https://pokeapi.co/api/v2/pokemon/bulbasaur'   # SE DIGITAR ERRADO VOLTA O BULBASAURO
        r = requests.get(api_link)
    dados = json.loads(r.text)                                      # TRANSFORMA O JSON DA API EM UM OBJETO PYTHON

    img = dados['sprites']['front_default']
    poke_img = urllib.request.urlretrieve(img, 'poke.png')          # BAIXA A IMAGEM PELA URL E SALVA COMO 'poke.png'
    diminuirImagem('poke.png')                                      # FUNÇÃO QUE RETIRA O FUNDO PRETO E DEIXA O MENOR POSSÍVEL

    poke_img = Image.open(poke_img[0])                              # PRECISA DO [0] PORQUE É UMA TUPLA ONDE O SEGUNDO ITEM É O CABEÇALHO DO RETORNO HTTP
    largura, altura = poke_img.size                                 # VALORES DE ALTURA E LARGURA DA IMAGEM ORIGINAL
    print(poke_img)
    altura_nova = altura*3                                          # MULTIPLICA EM 3 O TAMANHO DA IMAGEM
    largura_nova = largura*3                                        #
    poke_img = poke_img.resize((largura_nova, altura_nova))         # REDIMENSIONA MANTENDO AS PROPORÇÕES
    poke_img = ImageTk.PhotoImage(poke_img)                         # TRANSFORMA EM UM FORMATO COMPATIVEL COM O TKINTER
    poke_img_ready = Label(frameMeio, image=poke_img, bg='#ffffff') # POSICIONA NO FRAME DO MEIO

    poke_img_ready.place(x = 180 - (largura_nova / 2) + 10, y = 120 - (altura_nova // 2 ) + 20   )
    # 180 É METADE DE 360, QUE É O TAMANHO DO VISOR (SÓ A PARTE BRANCA)
    # O 10 SOMADO EM X É PRA COMPENSAR A PEQUENA BORDA MAIS ESCURA QUE SÓ TEM DO LADO ESQUERDO
    # 120 É METADE DE 240, QUE É A LARGURA DO VISOR (SÓ A PARTE BRANCA)
    # O 20 SOMADO É PARA COMPENSAR A BORDA DE CIMA QUE TEM EXATAMENTE 20 PIXEIS. ELA É PRA IMPEDIR QUE OS SPRITES GRANDES SEJAM PROJETADOS EM CIMA DA BORDA DO VISOR



# CRIANDO A LABEL COM O TEXTO
l_palavra = Label(frameCima, text='Digite o nome de um pokemon', height=1, anchor=NW, font='Ivy 11', bg=vermelho, fg=cinza_claro)
l_palavra.place(x=7, y=15)

# CRIANDO  O INPUT PARA DIGITAR O NOME DO POKEMON
e_palavra = Entry(frameCima, width=18, font=('Ivy 14 '), justify='center',relief="solid")
e_palavra.place(x=10, y=41)

# CRIANDO O BOTÃO E ASSOCIANDO A ELE A FUNÇÃO DE PROCURAR O POKEMON NA API
b_procurar = Button(frameCima,command=procurar, compound=CENTER,width=10, text='Procurar' ,bg=azul_claro,font=('Ivy 11'), overrelief=RIDGE,)
b_procurar.place(x=260, y=40)




janela.mainloop()