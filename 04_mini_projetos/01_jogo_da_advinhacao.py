import random
import os


def limpar_terminal():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


def jogar():
  vidas = 5
  palpites = []

  dificuldades = {'f': 10, 'm': 50, 'd': 100}
  nivel = input(
      'Selecione o nivel de dificuldade: [F]acil [M]edio [D]ificil: ')
  limpar_terminal()
  if nivel in dificuldades:
    nivel_escolhido = dificuldades[nivel]
    numero_secreto = random.randint(1, nivel_escolhido)

  while True:
    chute = int(input(f'Digite um numero entre 1 e {nivel_escolhido}: '))
    palpites.append(chute)
    limpar_terminal()
    print(f'Palpites {palpites}')
    if chute == numero_secreto:
      print(f'Parabéns, você acertou o numero {numero_secreto}')
      break
    elif chute < numero_secreto:
      vidas -= 1
      if vidas <= 0:
        print('Game over!')
        break
      print('Você errou, tente um numero maior!')
      continue
    elif chute > numero_secreto:
      vidas -= 1
      if vidas <= 0:
        print('Game over!')
        break
      print('Você errou, tente um numero menor!')
      continue


def main():
  print('Bem vindo ao jogo da advinhação!')
  jogar()
  while True:
    jogar_novamente = input('Deseja jogar novamente? [S]im [N]ão: ').upper()
    if jogar_novamente == 'S':
      jogar()
    else:
      break


main()