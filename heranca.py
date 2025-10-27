class Pessoa:
    def __init__(self, nome: None, cpf: None):
        self.nome = nome
        self.cpf = cpf

    def apresentar(self) -> str:
        return f'Olá, eu sou {self.nome}'


class Aluno(Pessoa):
    def __init__(self, nome = None, matricula = None, cpf = None):

        if nome is None:
            nome = input('Digite seu nome: ')

        if matricula is None:
            matricula = input('Digite sua matricula: ')

        if cpf is None:
            cpf = input('Digite seu cpf: ')

        super().__init__(nome, cpf)
        self.matricula = matricula

    def apresentar(self) -> str:
        base = super().apresentar()
        return f'{base} e sou aluno, matricula {self.matricula}'
    

class Professor(Aluno):
    def __init__(self, nome = None, disciplina = None, cpf = None):

        if nome is None:
            nome = input('digite seu nome: ')

        if cpf is None:
            cpf = input('digite seu cpf: ')

        if disciplina is None:
            disciplina = input('digite sua disciplina: ')

        super().__init__(nome, disciplina, cpf)
        self.disciplina = disciplina

    def apresentar(self):
        base = super().apresentar()
        return f'Professor {self.nome} de {self.disciplina}'


#programa principal
pessoa = Pessoa('Joao', '123.456.789.00')
aluno = Aluno()
professor = Professor()

print(pessoa.apresentar())
print(aluno.apresentar())
print(professor.apresentar())