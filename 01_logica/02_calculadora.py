#calculadora simples
def calculadora(a, b, operacao):
  if operacao == '+':
    return a + b
  elif operacao == '-':
    return a - b
  elif operacao == '/':
    if b == 0:
      print('Erro divisão por zero')
    return a / b
  elif operacao == '*':
    return a * b
  else:
    return 'Operação invalida'


print(calculadora(10, 5, '+'))
print(calculadora(10, 5, '-'))
print(calculadora(10, 5, '/'))
print(calculadora(10, 5, '*'))
