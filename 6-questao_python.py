import json
import os



def carregar_tarefas():
    if os.path.exists("tarefas.json"):
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    else:
        return []



def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)



def adicionar_tarefa(tarefas):
    descricao = input("Digite a tarefa: ")
    nova_tarefa = {"tarefa": descricao, "concluida": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada!")



def listar_tarefas(tarefas):
    if not tarefas:
        print("Sem tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. [{status}] {tarefa['descricao']}")



def marcar_tarefa_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa concluída.")
        else:
            print("Número inválido.")
    except ValueError:
        print("digite um número válido.")



def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que quer remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print(f"Tarefa removida: {tarefa_removida['descricao']}")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("digite um número válido.")



def main():
    tarefas = carregar_tarefas()
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            marcar_tarefa_concluida(tarefas)
        elif escolha == "4":
            remover_tarefa(tarefas)
        elif escolha == "5":
            break
        else:
            print("Opção inválida. tente novamente.")


if __name__ == "__main__":
    main()