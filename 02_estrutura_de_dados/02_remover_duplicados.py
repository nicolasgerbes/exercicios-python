#remove itens duplicados de uma lista

lista_nova = []
lista = ['banana', 'maçã', 'laranja', 'banana', 'abacaxi']

for fruta in lista:
  if fruta in lista_nova:
    pass
  else:
    lista_nova.append(fruta)

print(lista_nova)