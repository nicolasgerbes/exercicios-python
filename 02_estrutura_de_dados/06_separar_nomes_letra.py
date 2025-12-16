#Separa nomes em um dicionario pela primeira letra

lista_nomes = []

def criar_lista():
  while True:
    nomes = input('Digite os nomes [S]air: ')
    lista_nomes.append(nomes)
    if nomes.upper() == "S":
      print()
      break
    
def agrupar_primeira_letra(nomes):
  criar_lista()
  grupos = {}  # dicionário que vai guardar as listas

  for nome in nomes:
    if nome:  # garante que não é string vazia
      primeira_letra = nome[0].upper()

      # se ainda não existe a letra no dicionário, cria a lista
      if primeira_letra not in grupos:
        grupos[primeira_letra] = []

      grupos[primeira_letra].append(nome)

  return grupos



resultado = agrupar_primeira_letra(lista_nomes)

# imprime cada chave e seus nomes separados por vírgula
for letra, nomes in resultado.items():
  nomes_str = ", ".join(nomes) # junta os nomes com vírgula
  print(f'{letra}: {nomes_str}')
  