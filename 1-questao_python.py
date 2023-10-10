def calcular_nota(media):
    if media >= 90:
        return 'A'
    elif media >= 80:
        return 'B'
    elif media >= 70:
        return 'C'
    elif media >= 60:
        return 'D'
    else:
        return 'F'



def main():

    num_notas = int(input("Quantas notas você quer inserir? "))


    soma_notas = 0


    for i in range(num_notas):
        nota = float(input(f"Informe a nota {i + 1}: "))
        soma_notas += nota


    media = soma_notas / num_notas


    nota_correspondente = calcular_nota(media)


    print(f"Sua média é {media:.2f} e sua nota é {nota_correspondente}")


if __name__ == "__main__":
    main()
