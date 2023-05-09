from poke_assistant import *
from Pokedex import *
from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk, ImageSequence

frame_index = 0
id_chamada = None

def mostrar_pokemon():
    global frame_index
    global img_atual
    global id_chamada

    if id_chamada is not None:
        root.after_cancel(id_chamada) #cancela a chamada anterior
                                      #para que a animação não fique acelerada



    gif_path = './img/poke.gif'
    gif = Image.open(gif_path)
    if frame_index >= gif.n_frames:
        frame_index = 0
    gif.seek(frame_index)

    img_atual = ImageTk.PhotoImage(gif)

    largura = img_atual.width()
    altura = img_atual.height()
    img_label.place(x=math.floor(200 - (largura / 2)),
                    y = 20)
    img_label.configure(image=img_atual, background='#ffffff')
    frame_index += 1

    id_chamada = root.after(100, mostrar_pokemon)

def pesquisando(event):

    nome_pokemon = Pokedex_obj.e_palavra.get()
    assistente = Pesquisador_Pokemon(nome_pokemon)
    url_poke = assistente.pegar_url(nome_pokemon)
    r = assistente.retornar_resposta(url_poke)
    json = assistente.retorna_json(r)

    pokemon = Pokemon(
        nome = assistente.retorna_nome(json),
        tipos = ', '.join(assistente.retorna_tipos(json)),
        habilidades= ', '.join(assistente.retorna_habilidades(json)),
        url_gif = assistente.retorna_link_gif(json)
    )
    assistente.retorna_gif(pokemon.url_gif)
    assistente.retorna_gif_sem_fundo()

    mostrar_pokemon()

root = Tk()
Pokedex_obj = Pokedex(root)

# CRIANDO LABEL VAZIO
img_label = Label(Pokedex_obj.frameMeio, image='', borderwidth=-1)
img_label.place(x=0,
                y=0)

botao = Pokedex_obj.botao_procurar
botao.bind('<Button-1>', pesquisando)

root.mainloop()
