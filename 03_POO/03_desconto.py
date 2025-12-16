#Aplicar desconto em produto

class Produto:
  def __init__(self, nome, preco):
      self.nome = nome
      self.preco = preco

  def aplicar_desconto(self, percentual):
      if percentual <= 0 or percentual >= 100:
        print('Valor de desconto invalido')
        return False

      desconto = self.preco * (percentual / 100)
      self.preco -= desconto

  def desconto_aplicado(self):
    print(f'Produto: {self.nome}, Preço: {self.preco:.2f}R$')


p1 = Produto('iPhone', 3000)
print(p1.aplicar_desconto(10))
print(p1.desconto_aplicado())