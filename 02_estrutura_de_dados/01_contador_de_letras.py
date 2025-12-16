#cria um dicionario com a quantidade de letras

palavra = input('Digite uma palavra: ')

contador = {}
for letra in palavra:
  if letra in contador:
    contador[letra] += 1
  elif letra not in contador:
    contador[letra] = 1
print(f'A palavra contem {contador}')


