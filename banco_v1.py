import textwrap


class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito:\tR$ {valor:.2f}")
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor, limite=500, limite_saques=3):
        if self.numero_saques >= limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques diários excedido. @@@")
        elif valor > self.saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
        elif valor > limite:
            print("\n@@@ Operação falhou! Valor excede o limite de saque. @@@")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque:\t\tR$ {valor:.2f}")
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

    def exibir_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in self.extrato:
                print(movimentacao)
            print(f"\nSaldo atual: R$ {self.saldo:.2f}")


def menu():
    menu_texto = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    Escolha uma opção: """
    return input(textwrap.dedent(menu_texto)).lower().strip()


def main():
    conta = ContaBancaria()

    while True:
        opcao = menu()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                conta.depositar(valor)
            except ValueError:
                print("\n@@@ Por favor, insira um número válido. @@@")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: R$ "))
                conta.sacar(valor)
            except ValueError:
                print("\n@@@ Por favor, insira um número válido. @@@")

        elif opcao == "e":
            conta.exibir_extrato()

        elif opcao == "q":
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()