class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: O valor do depósito deve ser maior que zero.")
            return False
        self.saldo += valor
        return True

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser maior que zero.")
            return False
        if valor > self.saldo:
            print("Erro: Saldo insuficiente para realizar o saque.")
            return False
        self.saldo -= valor
        return True

    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False
