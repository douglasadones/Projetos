from pygame import mixer
from random import randint
from PIL import Image


def playmusic(msg):
    mixer.init()
    mixer.music.load(msg)
    mixer.music.play()
    mixer.music.set_volume(0.9)


def tratando_erros_int(parametro, msg):
    while parametro < 0:
        try:
            parametro = int(input(msg))
            if parametro < 0:
                print('Hm...')
        except ValueError:
            print('Hm....')
    return parametro


def tratando_erros_str(parametro, msg):
    while parametro not in 'SN':
        try:
            parametro = str(input(msg)).strip().upper()[0]
            if parametro not in 'SN':
                print('Hm...')
        except ValueError:
            print('Hm....')
    return parametro


def imagem(a, b):
    n = randint(a, b)
    im = Image.open(f'img{n}.jpg')
    im.show()
