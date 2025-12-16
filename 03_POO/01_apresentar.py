class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    print(f'{self.nome} tem {self.idade} anos de idade')


p1 = Pessoa('Maria Eduarda', 18)
p1.apresentar()