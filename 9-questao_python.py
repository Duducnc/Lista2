9- 

import json


filmes = [
    {"id": 1, "titulo": "Filme A", "horarios": ["10:00", "13:00", "16:00"]},
    {"id": 2, "titulo": "Filme B", "horarios": ["11:00", "14:00", "17:00"]},
    {"id": 3, "titulo": "Filme C", "horarios": ["12:00", "15:00", "18:00"]}
]

def mostrar_filmes():
    print("Filmes disponíveis:")
    for filme in filmes:
        print(f"{filme['id']}. {filme['titulo']}")

def mostrar_horarios(filme_id):
    for filme in filmes:
        if filme["id"] == filme_id:
            print(f"Horários disponíveis para {filme['titulo']}:")
            for horario in filme["horarios"]:
                print(horario)

def fazer_reserva():
    mostrar_filmes()
    filme_id = int(input("Escolha o filme pelo ID: "))

    if filme_id < 1 or filme_id > len(filmes):
        print("ID de filme inválido.")
        return

    mostrar_horarios(filme_id)
    horario = input("Escolha o horário: ")

    
    for filme in filmes:
        if filme["id"] == filme_id and horario not in filme["horarios"]:
            print("Horário indisponível.")
            return

    nome = input("Digite seu nome: ")
    num_ingressos = int(input("Por favor, indique a quantidade de ingressos que você gostaria de adquirir."))

    reserva = {
        "filme": filmes[filme_id - 1]["titulo"],
        "horario": horario,
        "nome": nome,
        "num_ing": num_ingressos
    }

    with open("reservas.txt", "a") as arquivo:
        arquivo.write(json.dumps(reserva) + "\n")

    print("Reserva confirmada com êxito!")

def main():
    while True:
        print("\nSistema de Reservas de Cinema")
        opcao = input("1. Fazer reserva\n2. Sair\nEscolha uma opção: ")

        if opcao == "1":
            fazer_reserva()
        elif opcao == "2":
            break
        else:
            print("Escolha não válida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()