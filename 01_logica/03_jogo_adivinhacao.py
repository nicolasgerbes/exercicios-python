#Jogo da adivinhação

import random

def jogar():
  palpites=[]
  numero_secreto = random.randint(0, 100)

  
  while True:
    chute = input('Digite um numero entre 1 e 100: ')
    palpites.append(chute)

    if chute == numero_secreto:
      print('parabéns você acertou')
      break
    else:
      print('você errou, tente novamente')
      continue


jogar()