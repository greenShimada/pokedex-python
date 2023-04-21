from poke_assistant import *
from Pokedex import *
from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk

frame_index = 0
def mostrar_pokemon():
    global frame_index
    global img_atual

    gif_path = './img/poke.gif'
    gif = Image.open(gif_path)

    gif.seek(frame_index)
    gif_maior = gif.resize((150, 150))
    img_atual = ImageTk.PhotoImage(gif_maior)

    largura = img_atual.width()
    altura = img_atual.height()
    img_label.place(x=200 - (largura/2),
                    y = 20)
    img_label.configure(image=img_atual, background='#ffffff')
    frame_index += 1
    if frame_index >= gif.n_frames:
        frame_index = 0


    root.after(200, mostrar_pokemon)

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
    mostrar_pokemon()

root = Tk()
Pokedex_obj = Pokedex(root)
# CRIANDO LABEL VAZIO
img_label = Label(Pokedex_obj.frameMeio, image='')
img_label.place(x=0,
                y=0)
botao = Pokedex_obj.botao_procurar
botao.bind('<Button-1>', pesquisando)



root.mainloop()
