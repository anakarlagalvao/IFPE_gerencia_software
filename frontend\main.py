from backend.conta import Conta

def main():
    contas = {}

    while True:
        print("\n--- SISTEMA BANCÁRIO ---")
        print("1. Cadastrar Conta")
        print("2. Consultar Saldo")
        print("3. Crédito (Depósito)")
        print("4. Débito (Saque)")
        print("5. Transferência")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Digite o número da conta: ")
            if numero in contas:
                print("Conta já existe!")
            else:
                contas[numero] = Conta(numero)
                print(f"Conta {numero} cadastrada com sucesso!")

        elif opcao == "2":
            numero = input("Digite o número da conta: ")
            if numero in contas:
                print(f"Saldo atual: R$ {contas[numero].consultar_saldo():.2f}")
            else:
                print("Conta não encontrada!")

        elif opcao == "3":
            numero = input("Digite o número da conta: ")
            if numero in contas:
                valor = float(input("Digite o valor do crédito: "))
                contas[numero].depositar(valor)
                print("Crédito realizado com sucesso!")
            else:
                print("Conta não encontrada!")

        elif opcao == "4":
            numero = input("Digite o número da conta: ")
            if numero in contas:
                valor = float(input("Digite o valor do débito: "))
                if contas[numero].sacar(valor):
                    print("Débito realizado com sucesso!")
                else:
                    print("Saldo insuficiente ou valor inválido!")
            else:
                print("Conta não encontrada!")

        elif opcao == "5":
            origem = input("Número da conta de origem: ")
            destino = input("Número da conta de destino: ")
            if origem in contas and destino in contas:
                valor = float(input("Digite o valor da transferência: "))
                if contas[origem].sacar(valor):
                    contas[destino].depositar(valor)
                    print("Transferência realizada com sucesso!")
                else:
                    print("Saldo insuficiente na conta de origem!")
            else:
                print("Conta de origem ou destino não encontrada!")

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
