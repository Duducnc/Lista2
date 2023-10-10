import random


palavras = ["python", "programacao", "computador", "jogos", "internet", "desenvolvedor"]



def escolher_palavra():
    return random.choice(palavras)



def jogar_forca():
    palavra = escolher_palavra()
    palavra_escondida = ["_" for _ in palavra]
    tentativas = 6

    while tentativas > 0 and "_" in palavra_escondida:
        letra = input("\nDigite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if letra in palavra:
            print("Letra correta!")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_escondida[i] = letra
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas -= 1

        print("Palavra: " + " ".join(palavra_escondida))
        print(f"Tentativas restantes: {tentativas}")

    if "_" not in palavra_escondida:
        print("\nParabéns, você venceu! A palavra era: " + palavra)
    else:
        print("\nVocê perdeu. A palavra era: " + palavra)



def main():
    print("Bem-vindo ao Jogo da Forca!")
    while True:
        jogar_forca()
        novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if novamente != "s":
            break


if __name__ == "__main__":
    main()