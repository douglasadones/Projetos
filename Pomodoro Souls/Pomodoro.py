from defpomodoro import *
from time import sleep

# Programa Principal
print('*' * 50)
print(f'{"POMODORO SOULS":^50}')
print('*' * 50)


# Solicitação de informações + Sistema Anti-Erro
while True:
    ativo = descanso = ciclos = -1
    r = ' '
    rr = 'S'
    ativo = validaçãoint(ativo, 'Informe o Tempo ativo (em minutos): ')
    descanso = validaçãoint(descanso, 'Informe o Tempo de descanso (em minutos):  ')
    ciclos = validaçãoint(ciclos, 'Quantos ciclos? ')
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
        print('Pomodoro Concluído!')


# Solicitação de Informações para Encerramento / Repetição do Programa.
        r = validaçãostr(r, 'Deseja iniciar novamente? [S/N] ')
        if r == 'S':
            rr = validaçãostr(rr, 'Deseja manter os mesmos parâmetros? [S/N] ')
    if r == 'N':
        break
print('Programa finalizado.')
