from pygame import mixer
from random import randint
from PIL import Image
from time import localtime


def playmusic(msg):
    mixer.init()
    mixer.music.load(msg)
    mixer.music.play()
    mixer.music.set_volume(0.9)


def tratando_erros_int(msg):
    while True:
        try:
            parametro = int(input(msg))
            if parametro < 0:
                print('Hm...')
            else:
                break
        except ValueError:
            print('Hm....')
    return parametro


def tratando_erros_str(msg):
    while True:
        try:
            parametro = str(input(msg)).strip().upper()[0]
            if parametro not in 'SN':
                print('Hm...')
            else:
                break
        except (ValueError, IndexError):
            print('Hm....')
    return parametro


def imagem(a, b):
    n = randint(a, b)
    im = Image.open(f'img{n}.jpg')
    im.show()


def hora_inicio_e_fim(tempo):
    horas = localtime().tm_hour
    minutos = localtime().tm_min
    print(f"Iniciado às {horas:0>2}:{minutos:0>2}")
    if minutos + tempo >= 60:
        horas += (minutos + tempo) // 60
        minutos = (minutos + tempo) % 60
    else:
        minutos += tempo
    print(f"Encerra às {horas % 24:0>2}:{minutos:0>2}")

