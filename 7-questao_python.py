7- 

import random

def adivinhe_o_numero():
    numero_aleatorio = random.randint(1, 100)  
    tentativas = 0

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        try:
            tentativa = int(input("Digite sua tentativa: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1

        if tentativa < numero_aleatorio:
            print("Tente um número maior.")
        elif tentativa > numero_aleatorio:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número com precisão! {numero_aleatorio} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    adivinhe_o_numero()