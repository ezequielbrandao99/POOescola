class Animal:
    def __init__(self, nome):
        self.nome = nome
        def falar(self):
            print('som do animal')

class cachorro(Animal):
    def falar(self):
        print('vamo correr atrás de moto!')

class gato(Animal):
    def falar(self):
        print('vamo rasgar o sofá!')

dog = cachorro('junin')
cat = gato('cleitin')

dog.falar()
cat.falar()