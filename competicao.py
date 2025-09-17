def escola():

    print('EEEP PROFESSOR ONÉLIO PORTO\n')

    funcao = int(input('Qual a sua função na escola? ' \
    '\n1 - Gestor' \
    '\n2 - Professor' \
    '\n3 - Aluno'))

    if(funcao == 1):
        def gestor():
            escolha = input('oque deseja fazer? '
            '\n1 - verificar disposição de professores '
            '\n2 - verificar disposição de coordenadores '
            '\n3 - verificar disposição de zeladores '
            '\n4 - verificar disposição de cozinheiros '
            '\n1 - abrir seleção de professores '
            '\n2 - suspender aluno '
            '\n3 - notificar aluno '
            '\n4 - transferir aluno ')
            gestor()
            

    if(funcao == 2):
        materia = str(input('\nDigite a materia que leciona: '))
        escolha = int(input('\nOque deseja fazer? '
        '\n1 - adicionar nota no sistema '
        '\n2 - Lançar AVA '
        '\n3 - agendar recuperação parcial '
        '\n4 - agendar recuperação final '))

        if(escolha == 1):
            aluno = str('digite o nome do aluno: '
            '\ndigite a turma do aluno: '
            '\ndigite a nota do aluno: ')

            print('aluno: ', aluno)

    if(funcao == 4):
        escolha = int(input('oque deseja fazer? ' \
        '\n1 - calcular médias de notas: ' \
        '\n2 - Pedir carteira de estudante' \
        '\n3 - pedir isenção ENEM'))

    if(funcao == 5):
        escolha = int(input('oque deseja fazer? ' \
        '\n1 - chamar aluno ' \
        '\n2 - chamar coordenador ' \
        '\n3 - chamar diretor '))

escola()
