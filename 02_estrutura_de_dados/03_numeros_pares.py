#retorna apenas os numeros pares de uma lista

lista_numeros = [1, 2, 3, 4, 5, 6]
lista_pares = []

for n in lista_numeros:
  if n % 2 == 0:
    lista_pares.append(n)
  else:
    pass
print(lista_pares)