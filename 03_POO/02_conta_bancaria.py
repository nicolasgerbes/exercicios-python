#Sistema de Conta

class ContaBancaria:
  def __init__(self, titular, numero, saldo):
    self.titular = titular
    self.numero = numero
    self.saldo = saldo

  def depositar(self, valor):
    if valor <=0:
      print('Valor de desposito deve ser positivo.')
      return False
    self.saldo += valor
    return True

  def sacar(self, valor):
    if valor <= 0: 
      print('Valor de saque deve ser positivo.')
      return False
    if valor > self.saldo:
      print('Saldo Insuficiente')
      return False
    self.saldo -= valor
    return True

  def ver_saldo(self):
    return f'Saldo: {self.saldo}R$'

  def __str__(self):
    return f'Conta {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}'


c1 = ContaBancaria('Maria Eduarda', 2119, 2500)

print(c1.sacar(4500))
print(c1.depositar(5000))
print(c1.sacar(4500))
print(c1.ver_saldo())