class Hotel():
    def __init__(self, cor=None, quartos=None, banheiros=None, andares=None):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        self.andares = andares

    def estrutura(self):
        self.cor = input('Qual a cor do hotel?')
        self.andares = input('Quantos andares tem o hotel?')
        self.quartos = input('Quantos quartos tem o hotel?')
        self.banheiros = input('Quantos banheiros tem o hotel?')

    return f"Este hotel é {self.cor}, tem {self.andares} andares, {self.quartos} quartos e {self.banheiros} banheiros."

ht = Hotel()
print(ht.estrutura())

class Pessoa():
    def __init__(self, nome = None):
        self.nome = nome
        self.nome = input('Qual o seu nome?')

    def falar(self, mensagem = None)
        self.mensagem = input('Oque você quer dizer?')
        return f"{self.nome} disse: {self.mensagem}"

    def cantar(self, musica = None)
        self.musica = input('Oque você quer cantar?')
        return f"{self.nome} está cantando: {self.musica}"

    def estudar(self, materia = None)
        self.materia = input('Oque você quer estudar?')
        return f"{self.nome} está estudando: {self.materia}"

    def eu(self)
        return f"Meu nome é {self.nome}, e eu gostaria de falar {self.mensagem}, eu gosto de cantar a musica {self.musica} e estou estudandp {self.materia}."

p = Pessoa
p.falar
p.cantar
p.estudar
print(p.eu())