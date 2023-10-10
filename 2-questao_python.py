import csv
import os



def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")

    with open("agenda.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone])

    print("Contato adicionado com sucesso!")


def listar_contatos():
    with open("agenda.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Nome: {row[0]}, Telefone: {row[1]}")



def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")

    with open("agenda.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if nome.lower() in row[0].lower():
                print(f"Nome: {row[0]}, Telefone: {row[1]}")



def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")


    contatos = []

    with open("agenda.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if nome.lower() not in row[0].lower():
                contatos.append(row)


    with open("agenda.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        for contato in contatos:
            writer.writerow(contato)

    print("Contato removido com sucesso!")



def main():
    while True:
        print("\nAgenda de Contatos")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_contato()
        elif escolha == "2":
            listar_contatos()
        elif escolha == "3":
            buscar_contato()
        elif escolha == "4":
            remover_contato()
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    if not os.path.isfile("agenda.csv"):
        with open("agenda.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Telefone"])

    main()