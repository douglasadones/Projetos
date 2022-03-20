MENU = {
    "espresso": {
        "ingredientes": {
            "água": 50,
            "café": 18,
        },
        "custo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "água": 200,
            "leite": 150,
            "café": 24,
        },
        "custo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "água": 250,
            "leite": 100,
            "café": 24,
        },
        "custo": 3.0,
    }
}

recursos = {
    "água": 300,
    "leite": 200,
    "café": 100,
}


def checando_recursos():
    """Verifica se ainda há recursos retornando True ou False com um print caso seja False."""
    recurso = ""
    for recursos_atuais, recursos_necessarios in MENU[pedido]["ingredientes"].items():
        if recursos[recursos_atuais] < recursos_necessarios:
            recurso = recursos_atuais
            break
    if len(recurso) != 0:
        print(f"Desculpe, não há {recurso} o suficiente.")
        return False
    else:
        return True


def usando_recursos():
    """Usa os recursos conforme o pedido."""
    recursos["água"] -= MENU[pedido]["ingredientes"]["água"]
    if pedido != "espresso":
        recursos["leite"] -= MENU[pedido]["ingredientes"]["leite"]
    recursos["café"] -= MENU[pedido]["ingredientes"]["café"]


def verificador_de_entrada_int(pergunta):
    """Verifica se a moeda informada é válida retornando o seu valor."""
    while True:
        try:
            moeda = int(input(pergunta))
        except ValueError:
            print("Insira uma moeda válida")
        else:
            return moeda


def chegando_o_pagamento():
    """Verifica se há dinheiro suficiente e troco necessário, caso contrário devolve o dinheiro
    retornando Verdadeiro ou Falso com print"""
    if pagamento < MENU[pedido]["custo"]:
        print("Desculpe, dinheiro insuficiente. Dinheiro devolvido.")
        return False
    else:
        print(f"R${int((pagamento - MENU[pedido]['custo']) * 100) / 100:.2f} de troco.")
        print(f"Aqui está o seu {pedido} ☕. Aproveite!")
        return True


def relatorio():
    """Mostra os recursos restantes e o dinheiro acumulado"""
    for nome, restante in recursos.items():
        if nome != "café":
            print(f"{nome}: {restante}ml")
        else:
            print(f"{nome}: {restante}g")
    print(f"Dinheiro: ${dinheiro}")


# Main Program
print("Guia do usuário: digite 'relatório' para verificar os recursos ou 'desligar' para desligar")
pedido = ""
dinheiro = 0

# TODO: 6. Guarde o dinheiro recebido e os recursos restantes e pergunte novamente o que o cliente deseja
while pedido != "desligar":
    fazer_o_pedido = False

    while not fazer_o_pedido:
        # TODO: 1. Perguntar que tipo de café o cliente quer
        pedido = str(input("O que você gostaria? (espresso/latte/cappuccino): ")).strip().lower()

        # TODO: 2. Verifique se há recursos suficientes para fazer o pedido e realizá-lo.
        if pedido == "espresso" or pedido == "latte" or pedido == "cappuccino":
            fazer_o_pedido = checando_recursos()
            if fazer_o_pedido:

                # TODO: 4. Pergunte separadamente quantas moedas.
                centavos = verificador_de_entrada_int("Quantas moedas de R$ 0,10 centavos? ") * 0.10
                centavos += verificador_de_entrada_int("Quantas moedas de R$ 0,25 centavos? ") * 0.25
                centavos += verificador_de_entrada_int("Quantas moedas de R$ 0,50 centavos? ") * 0.50
                real = verificador_de_entrada_int("Quantas moedas de R$ 1 real? ")

                # TODO: 5. Adicione tudo e verifique se você tem dinheiro suficiente para o pedido.
                pagamento = centavos + real
                fazer_o_pedido = chegando_o_pagamento()
                if fazer_o_pedido:
                    dinheiro += MENU[pedido]["custo"]
                    usando_recursos()

        # TODO: 3. Ser capaz de mostrar os recursos restantes quando "relatório" for digitado.
        elif pedido in "relatoriorelatório":
            if recursos["café"] == 100:
                dinheiro = 0
            relatorio()
        else:
            # TODO: 7. Desligar quando "desligar" for digitado
            if pedido in "desligar":
                break
