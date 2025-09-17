def cadastro():
    print('BEM-VINDO AO SISTEMA HOSPITALAR')
    
    idade = int(input('Digite sua idade: '))
    
    if(idade <18):
        print('O cadastro não foi realizado! Volte quando for maior de idade.')
    
    else:
        print('Cadastro realizado com sucesso!')

        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF: ')
        endereco = input('Digite seu endereço: ')
        tiposangue = input('Digite seu tipo sanguíneo: ')

        print('-----FICHA DE CADASTRO-----')
        print('-----DADOS DO USUÁRIO-----')
    
        print('Seu nome é: ', nome)
        print('Seu CPF é: ', cpf)
        print('Seu endereco é: ', endereco)
        print('Seu tipo sanguíneo é: ', tiposangue)
        print('Sua idade: ', idade)

cadastro()