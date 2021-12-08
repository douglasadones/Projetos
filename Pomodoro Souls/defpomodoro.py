from pygame import mixer


def playmusic():
    mixer.init()
    mixer.music.load('BF.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.9)


def validaçãoint(parametro, msg):
    while parametro < 0:
        try:
            parametro = int(input(msg))
            if parametro < 0:
                print('Hm...')
        except:
            print('Hm....')
    return parametro


def validaçãostr(parametro, msg):
    while parametro not in 'SN':
        try:
            parametro = str(input(msg)).strip().upper()[0]
            if parametro not in 'SN':
                print('Hm...')
        except:
            print('Hm....')
    return parametro