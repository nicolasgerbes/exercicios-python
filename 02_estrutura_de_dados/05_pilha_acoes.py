
#Pilhas para controlar ações
undo_stack = []
redo_stack = []

def executar_acao(acao):
    '''Executa uma ação e guarda a pilha de undo'''
    print(f'Ação executada: {acao}')
    undo_stack.append(acao)
    redo_stack.clear() #sempre que há uma nova ação limpa o redo

def undo():
    '''Desfaz a última ação'''
    if undo_stack:
        acao = undo_stack.pop()
        print(f'Desfazendo: {acao}')
        redo_stack.append(acao)
    else:
        print('Nada para desfazer')

def redo():
  '''Refaz a ultima ação desfeita'''
  if redo_stack:
    acao = redo_stack.pop()
    print(f'Refazendo: {acao}')
    undo_stack.append(acao)
  else:
    print('Nada para refazer')


executar_acao('Escrevendo linha 1')
executar_acao('Escrevendo linha 2')
executar_acao('Escrevendo linha 3')

undo()
undo()
redo()

print('\nEstado final')
print('Undo stack', undo_stack)
print('Redo stack', redo_stack)