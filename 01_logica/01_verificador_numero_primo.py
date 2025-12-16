#verificar se um numero é primo ou não

def num_primo(n):
    if n <= 1:
      return False

    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
          return False

    return True

numero = int(input('Digite um numero: '))
if num_primo(numero):
  print(f'{numero} é primo')
else:
  print(f'{numero} não é um numero primo')