from poke_assistant import *
from Pokedex import *
from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk, ImageSequence

frame_index = 0
id_chamada = None

def exibir(pokemon):

    str = '\n'
    controle_altura = 45
    label_nome = Pokedex_obj.labelNome
    label_nome.configure(text='')
    label_nome.configure(text='NOME: ' + pokemon.nome.title())

    label_habilidades = Pokedex_obj.labelHabilidade
    label_habilidades.configure(text='')

    label_nome.place(x=15, y=20)
    label_habilidades.place(x=15, y=45)
    for i in pokemon.habilidades:
        str = str + i + " "
    label_habilidades.configure(text='HABILIDADES: ' + str)
    print(pokemon.tipos)

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
                    y = 330 - altura)
    img_label.configure(image=img_atual, background='#ffffff')
    frame_index += 1

    id_chamada = root.after(100, mostrar_pokemon)

def pesquisando(event):
    nome_pokemon = Pokedex_obj.e_palavra.get()
    assistente = Pesquisador_Pokemon(nome_pokemon)
    url_poke = assistente.pegar_url(nome_pokemon)
    r = assistente.retornar_resposta(url_poke)
    json = assistente.retorna_json(r)
    bg = Pokedex_obj.bg
    pokemon = Pokemon(
        nome = assistente.retorna_nome(json),
        tipos = assistente.retorna_tipos(json),
        habilidades= assistente.retorna_habilidades(json),
        url_gif = assistente.retorna_link_gif(json)
    )
    if pokemon.tipos[0] == 'Fire':
        bg = './bg/newFire.jpg'
    elif pokemon.tipos[0] == 'Flying':
        bg = './bg/newAir.jpg'
    elif pokemon.tipos[0] == 'Water':
        bg = './bg/newWater.jpg'
    else:
        bg = './bg/newTerrain.jpg'
    assistente.altera_fundo(bg, Pokedex_obj)
    exibir(pokemon)
    assistente.retorna_gif(pokemon.url_gif)
    assistente.retorna_gif_sem_fundo(bg)
    mostrar_pokemon()

root = Tk()
Pokedex_obj = Pokedex(root)

# CRIANDO LABEL VAZIO
img_label = Label(Pokedex_obj.frameEsquerda, image='', borderwidth=-1)
img_label.place(x=0,
                y=0)

botao = Pokedex_obj.botao_procurar
botao.bind('<Button-1>', pesquisando)

root.mainloop()
