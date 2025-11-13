class carro:
    def abrir_porta(self):
        print('a porta do carro está aberta')

    def abrir_janela(self):
        print('a janela do carro está aberta')

    def acelerar(self):
        print('o carro está acelerando')

class casa:
    def abrir_porta(self):
        print('a porta da casa está aberta')

    def abrir_janela(self):
        print('a janela da casa está aberta')

class moto:
    def acelerar(self):
        print('a moto está acelerando')

    def abrir_porta(self):
        print('a moto não tem porta para abrir')

def acelerar(obj):
    obj.acelerar()

def abrir_porta(obj):
    obj.abrir_porta() 


c = carro()
cs = casa()
m = moto()

objetos = [casa(), carro(), moto()]

for obj in objetos:
    abrir_porta(obj)