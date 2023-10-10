class ContaBancaria:
    def __init__(self, saldo_inic=0):
        self.saldo = saldo_inic
    def consultar_saldo(self):
        return self.saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "Valor de depósito inválido."
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        else:
            return "Saldo insuficiente."
def main():
    conta = ContaBancaria()
    while True:
        print("\n===== Caixa Eletrônico =====")
        print("1. Consultar Saldo")
        print("2. Depositar Dinheiro")
        print("3. Sacar Dinheiro")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == "1":
            saldo = conta.consultar_saldo()
            print(f"Saldo atual: R${saldo:.2f}")
        elif opcao == "2":
            valor = float(input("Informe o valor a ser depositado: R$"))
            mensagem = conta.depositar(valor)
            print(mensagem)
        elif opcao == "3":
            valor = float(input("Informe o valor a ser sacado: R$"))
            mensagem = conta.sacar(valor)
            print(mensagem)
        elif opcao == "4":
            print("Obrigado por usar Caixa Eletrônico. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()