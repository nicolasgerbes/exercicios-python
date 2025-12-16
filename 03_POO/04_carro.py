class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, aumentar):
        self.velocidade += aumentar
        print(f'O carro acelerou para {self.velocidade} km/h')


    def frear(self, reduzir):
        self.velocidade -= reduzir
        if self.velocidade <= 0:
            self.velocidade = 0
        print(f'O carro reduziu para {self.velocidade} km/h')


carro1 = Carro('Toyota', 'Corola', 2022, 0)

carro1.acelerar(70)
carro1.acelerar(100)
carro1.frear(60)