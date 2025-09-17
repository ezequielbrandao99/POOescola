'''def menu():
    print('BEM VINDO!')
    print('ESCOLHA SUA FUNÇÃO NA ESCOLA:')
    funcao = int(input('1 - Aluno' \
    '\n2 - Professor' \
    '\n3 - Gestor'))

    if funcao == 1:
        aluno()
    if funcao == 2:
        professor()
    if funcao == 3:
        gestor()

def aluno():
        
    print('-----MENU ALUNO-----')
    print('Escolha oque quer fazer: ')
    print('1 - Ver notas' \
    '\n2 - calcular medias')
    funcaoaluno = int(input(''))

    if funcaoaluno == 1:
        print('Notas: xxx' \
        '\nportugues: xxx' \
        '\nmatematica: xxx' \
        '\nbiologia: xxx' \
        '\nfilosofia: xxx' \
        '\nfisica: xxx' \
        '\nP.O.O: xxx')

    if funcaoaluno == 2:
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 1: '))
        n3 = float(input('Nota 1: '))

        media = (n1 + n2 + n3)/3

        print('Sua média atual é: ', media)

def professor():
    print('-----MENU PROFESSOR-----')
    print('Escolha oque quer fazer: ')
    print('1 - Adicionar notas' \
    '\n2 - Ver alunos')

def gestor():
    print('-----MENU GESTOR-----')
    print('Escolha oque quer fazer: ')
    print('1 - Ver funcionários' \
    '\n2 - Ver alunos' \
    '\n3 - Realizar notificação')

menu()'''

def cadastro():
    print('\nCadastro obrigatório! Realize-o para seguir na aplicação.')
    nome = str(input('\nDigite seu nome: '))
    idade = int(input('Digite sua idade: '))
    cpf = int(input('Digite seu cpf: '))
    endereco = str(input('digite seu endereço: '))

    print('CADASTRO REALIZADO!\n')
    print('Dados de usuário: ')
    print('nome: ', nome)
    print('idade: ', idade)
    print('CPF: ', cpf)
    print('Endereço: ', endereco)

cadastro()