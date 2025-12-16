#sistema de atendimento de clientes

fila = []
senhas = 0

def chegada(pessoa):
  global senhas
  senhas += 1
  fila.append([pessoa, senhas])

def atender():
  if fila:
    pessoa, senha = fila.pop(0)
    print(f'{pessoa} com senha {senhas} esta sendo atendido')
  else:
    print('Nenhuma pessoa na fila')
  
chegada('Duda')
chegada('Nícolas')
chegada('Pessoa3')
chegada('Pessoa4')

print(f'Total de senhas geradas: {senhas}')

atender()
atender()
atender()