#palindromo

def palindromo(texto):
  texto = texto.lower().replace(" ", "")
  return texto == texto[::-1]

print(palindromo('arara'))
print(palindromo('python'))
