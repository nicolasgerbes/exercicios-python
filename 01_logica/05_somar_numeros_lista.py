# Soma todos os numeros de uma lista

def somar_lista(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma

lista1 = input('Digite numeros separados por virgula: ').split(', ')
lista1 = (int(x) for x in lista1)

print(somar_lista(lista1))