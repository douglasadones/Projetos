from defpomodoro import *
from time import sleep

# Programa Principal
print("*" * 53)
print(f"{'POMODORO SOULS':^53}")
print("*" * 53)

# Solicitação de informações + Sistema Anti-Erro
while True:
    ativo = descanso = ciclos = -1
    loop = predefinido = imag = " "
    manter_parametros = "S"
    print(f"""{'Pomodoros Pré-definidos':^53}
[1] - Curto: 25min ativo + 05min descanso, 2 Ciclos
      Tempo Total: 1h
[2] - Padrão: 25min ativo + 05min descanso, 4 Ciclos 
      Tempo Total: 2h
[3] - Personalizado""")
    while predefinido not in "123":
        try:
            predefinido = str(input("Faça sua escolha, esqueleto: ")).strip()[0]
            if predefinido not in "123":
                print("hm...")
        except IndexError:
            print("hm...")
    if predefinido == "1":
        ativo, descanso, ciclos = 25, 5, 2
    elif predefinido == "2":
        ativo, descanso, ciclos = 25, 5, 4
    else:
        ativo = tratando_erros_int("Informe o Tempo ativo (em minutos): ")
        descanso = tratando_erros_int("Informe o Tempo de descanso (em minutos):  ")
        ciclos = tratando_erros_int("Quantos ciclos? ")
    imag = tratando_erros_str("Deseja ativar os alertas de imagem? [S/N] ")
    if ciclos == 0:
        ciclos = 1
    print(f"\n{'Pomodoro Iniciado':^53}\n")

# Execução do Programa com Base Nas Informações Solicitadas.
    while manter_parametros == "S":
        c = 1
        loop = " "
        manter_parametros = " "
        while c <= ciclos:
            playmusic("BF.mp3")
            if ativo != 0:
                print(f"Pomodoro ativo...")
                hora_inicio_e_fim(ativo)
                if imag == "S":
                    imagem(1, 7)  # fight
                if ciclos != 1:
                    if ciclos == c:
                        print(f"Contagem de ciclos: {c}° e último ciclo.")
                        print("\n")
                    else:
                        print(f"Contagem de repetições: {c}º Ciclo.")
                        print("\n")
                else:
                    print(f"Contagem de Ciclos: Ciclo único.")
                    print("\n")
                sleep(ativo * 60)
                playmusic("BF.mp3")

            # Para o uso padrão de um Pomodoro (ativo + descanso)
            if descanso != 0 and ciclos != c and ciclos != 1 and ativo != 0:
                print(f"Pomodoro para descanso... ")
                hora_inicio_e_fim(descanso)
                if imag == "S":
                    imagem(8, 12)  # bonfire
                if ciclos != 1:
                    if c + 1 == ciclos:
                        print(f"Contagem de Repetições: Preparando para o {c + 1}° e último ciclo.")
                        print("\n")
                    else:
                        print(f"Contagem de Repetições: Preparando para o {c + 1}° ciclo.")
                        print("\n")
                else:
                    print(f"Contagem de Ciclos: Ciclo único.")
                    print("\n")
                if ciclos != c:
                    sleep(descanso * 60)

            # Caso o tenha apenas o tempo de descanso
            if descanso != 0 and ativo == 0:
                print(f"Pomodoro para descanso...")
                hora_inicio_e_fim(descanso)
                if ativo == 0:
                    if ciclos != 1:
                        if ciclos == c:
                            print(f"Contagem de ciclos: {c}° e último ciclo.")
                            print("\n")
                        else:
                            print(f"Contagem de repetições: {c}º Ciclo.")
                            print("\n")
                    else:
                        print(f"Contagem de Ciclos: Ciclo único.")
                        print("\n")
                sleep(descanso * 60)
            c += 1
        playmusic("VG.mp3")
        if imag == "S":
            im = Image.open(f"fim.jpg")  # Fim
            im.show()
        print("Pomodoro Concluído!")

        # Solicitação de Informações para Encerramento / Repetição do Programa.
        loop = tratando_erros_str("Deseja iniciar novamente? [S/N] ")
        if loop == "S":
            manter_parametros = tratando_erros_str("Deseja manter os mesmos parâmetros? [S/N] ")
            print("\n")
    if loop == "N":
        break
print("Don't give up, skeleton!")
sleep(0.5)
