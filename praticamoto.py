#criando a classe
class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f'{self.modelo} acelerou para {self.velocidade} km/h!')

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f'{self.modelo} freou para {self.velocidade} km/h!')

    def detalhes(self):
        return (f'{self.marca} {self.modelo} ({self.ano}) -'
                f'cor: {self.cor}, velocidade: {self.velocidade} km/h')
    
#criando os objetos

moto1 = Moto("\nDucati", "Panigali V4s", 2024, "Vermelha")
moto2 = Moto("Kawasaki", "H2R", 2024, "Verde")

#interagindo com os objetos

print('\nSerá dada a largada na pista de 1/4 de milha!')
print('1')
print('2')
print('3')
print('Já')

print(moto1.detalhes())
print(moto2.detalhes())

moto1.acelerar(300)
moto2.acelerar(400)

moto1.frear(100)
moto2.frear(100)

print('''\nKawasaki wins!
      Velocidade máxima: 400km/h
      distância: 402 metros''')

print(moto1.detalhes())
print(moto2.detalhes())