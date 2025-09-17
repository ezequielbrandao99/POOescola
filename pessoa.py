class SerVivo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def respirar(self):
        print(f'{self.nome} está respirando...')

    def dormir(self):
        print(f'{self.nome} está dormindo...')

class pessoa(SerVivo):
    def falar(self, mensagem):
        print(f'{self.nome} diz: {mensagem}')

    def andar(self, destino):
        print(f'{self.nome} está andando até {destino}')
    
    def comer(self, comida):
        print(f'{self.nome} está comendo {comida}')

# Criando objetos
p1 = pessoa('Ezequiel', 16)
p2 = pessoa('Marco', 17)

# Chamando ações
p1.respirar()
p1.falar('eu sou um gênio')
p1.andar('Popular atacadista')
p1.comer('cuzcuz')

print('-------')

p2.dormir()
p2.falar('estou jogando Detroit')