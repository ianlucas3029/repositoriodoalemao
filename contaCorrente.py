from datetime import datetime
import pytz
from random import randint

class contaCorrente:    
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self.cpf = cpf
        self._saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self.transacoes.append((-valor, self._saldo, contaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino.transacoes.append((valor, conta_destino._saldo, contaCorrente._data_hora()))

    def consultar_saldo(self):
        return f'Seu saldo atual é de R${self._saldo:,.2f}'
    
    def depositar_dinheiro(self, valor):
        self._saldo += valor
        self.transacoes.append((valor, self._saldo, contaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar este valor!')
            print(self.consultar_saldo())
        else:
            self._saldo -= valor
            self.transacoes.append((valor, self._saldo, contaCorrente._data_hora()))

    def consultar_historico_transacoes(self):
        print("Histórico de transações: ")
        for transacao in self.transacoes:
            print(transacao)


conta_maeKalledy = contaCorrente("Kalledy", "111.222.333-45", 5555, 656565)
conta_Kalledy = contaCorrente("Kalledy", "111.222.333-45", 5555, 656565)



print(conta_Kalledy.consultar_saldo())
conta_Kalledy.depositar_dinheiro(10000)  


print(conta_Kalledy.consultar_saldo())
conta_Kalledy.sacar_dinheiro(1000)  

print(conta_Kalledy.consultar_saldo())


conta_Kalledy.transferir(1000, conta_maeKalledy)


print(conta_Kalledy.consultar_saldo())


print("O saldo da conta é: ", conta_Kalledy.consultar_saldo())
print(conta_Kalledy.cpf)

class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
