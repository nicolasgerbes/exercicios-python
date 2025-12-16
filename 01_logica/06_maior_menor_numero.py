#maior e menor numero de uma lista

def maior_e_menor(lista):
  maior = lista[0]
  menor = lista[0]

  for num in lista:
    if num > maior:
      maior = num
    if num < menor:
      menor = num

  return maior, menor

numeros = [3, 5, 7, 8, 3, 2]
maior, menor = maior_e_menor(numeros)
print(f'Maior numero {maior}')
print(f'Menor numero {menor}')