from defpomodoro import *
from time import sleep
from PIL import Image
from random import randint


def imagem(a, b):
    if imag == 'S':
        n = randint(a, b)
        im = Image.open(f'img{n}.jpg')
        im.show()


# Programa Principal
print('*' * 50)
print(f'{"POMODORO SOULS":^50}')
print('*' * 50)


# Solicitação de informações + Sistema Anti-Erro
while True:
    ativo = descanso = ciclos = -1
    r = ' '
    rr = 'S'
    imag = ' '
    ativo = validaçãoint(ativo, 'Informe o Tempo ativo (em minutos): ')
    descanso = validaçãoint(descanso, 'Informe o Tempo de descanso (em minutos):  ')
    ciclos = validaçãoint(ciclos, 'Quantos ciclos? ')
    imag = validaçãostr(imag, 'Deseja ativar os alertas de imagem? [S/N] ')
    if ciclos == 0:
        ciclos = 1


# Execução do Programa com Base Nas Informações Solicitadas.
    while rr == 'S':
        c = 1
        r = ' '
        rr = ' '
        while c <= ciclos:
            playmusic('BF.mp3')
            if ativo != 0:
                print('Pomodoro ativo...')
                imagem(1, 7)  # fight
                if ciclos != 1:
                    if ciclos == c:
                        print(f'Contagem de ciclos: {c}° e último ciclo.')
                    else:
                        print(f'Contagem de repetições: {c}º Ciclo.')
                else:
                    print(f'Contagem de Ciclos: Ciclo único.')
                sleep(ativo * 60)
                playmusic('BF.mp3')


            # Para o uso padrão de um Pomodoro (ativo + descanso)
            if descanso != 0 and ciclos != c and ciclos != 1 and ativo != 0:
                print('Pomodoro para descanso...')
                imagem(8, 12)  # bonfire
                if ciclos != 1:
                    if c + 1 == ciclos:
                        print(f'Contagem de Repetições: Preparando para o {c + 1}° e último ciclo.')
                    else:
                        print(f'Contagem de Repetições: Preparando para o {c + 1}° ciclo.')
                else:
                    print(f'Contagem de Ciclos: Ciclo único.')
                if ciclos != c:
                    sleep(descanso * 60)


            # Caso o tenha apenas o tempo de descanso
            if descanso != 0 and ativo == 0:
                print('Pomodoro para descanso...')
                if ativo == 0:
                    if ciclos != 1:
                        if ciclos == c:
                            print(f'Contagem de ciclos: {c}° e último ciclo.')
                        else:
                            print(f'Contagem de repetições: {c}º Ciclo.')
                    else:
                        print(f'Contagem de Ciclos: Ciclo único.')
                sleep(descanso * 60)
            c += 1
        playmusic('VG.mp3')
        if imag == 'S':
            im = Image.open(f'fim.jpg')  # Fim
            im.show()
        print('Pomodoro Concluído!')


# Solicitação de Informações para Encerramento / Repetição do Programa.
        r = validaçãostr(r, 'Deseja iniciar novamente? [S/N] ')
        if r == 'S':
            rr = validaçãostr(rr, 'Deseja manter os mesmos parâmetros? [S/N] ')
    if r == 'N':
        break
print('Programa finalizado!')
