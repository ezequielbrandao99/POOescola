def cadastro():
    print('\nCadastro obrigatório! Realize-o para seguir na aplicação.')
    nome = str(input('\nDigite seu nome: '))
    idade = int(input('Digite sua idade: '))
    cpf = int(input('Digite seu cpf: '))
    endereco = str(input('digite seu endereço: '))

    print('\nCADASTRO REALIZADO!\n')
    print('Dados de usuário: ')
    print('nome: ', nome)
    print('idade: ', idade)
    print('CPF: ', cpf)
    print('Endereço: ', endereco)

cadastro()

def menu():
    print('\nBEM VINDO À EEEP PROFESSOR ONÉLIO PORTO!\n')
    print('ESCOLHA SUA FUNÇÃO NA INSTITUIÇÃO:')
    funcao = int(input('1 - Aluno' \
    '\n2 - Professor' \
    '\n3 - Gestor\n'))

    if funcao == 1:
        aluno()
    if funcao == 2:
        professor()
    if funcao == 3:
        gestor()

def aluno():
        
    print('\n-----MENU ALUNO-----')

    print('\nEscolha oque quer fazer: ')
    print('1 - Ver notas' \
    '\n2 - calcular medias' \
    '\n')
    funcaoaluno = int(input(''))

    if funcaoaluno == 1:
        print('\nNotas: ' \
        '\nPortugues: 10' \
        '\nMatematica: 10' \
        '\nBiologia: 10' \
        '\nFilosofia: 10' \
        '\nFisica: 10' \
        '\nP.O.O: 10')
        n1 = float
    if funcaoaluno == 2:
        n1 = float(input('Nota 1: '))
        n2 = float(input('\nNota 2: '))
        n3 = float(input('\nNota 3: '))

        if n1>10 or n2>10 or n3>10:
            print('notas acima de 10 são inválidas, tente novamente.')
            exit()

        else:
            media = (n1 + n2 + n3)/3

        print('\nSua média atual é: ', media)

def professor():

    print('-----MENU PROFESSOR-----')

    nome = str(input('Olá professor! Por favor, digite seu nome: '))

    print('Agora, por favor, selecione a matéria que você leciona:')

    materia = int(input('\nmaterias: \n1 - Portugês' \
    '\n2 - matematica' \
    '\n3 - biologia' \
    '\n4 - filosofia' \
    '\n5 - fisica' \
    '\n6 - P.O.O' \
    '\n7 - ingles' \
    '\n8 - espanhol'))

    if materia == 1:
        print('Muito bem! Bem vindo profesor(a)', nome)
        print('Aqui está o seu painel de controle na disciplina de Português')

        print('Escolha oque quer fazer: ')
        funcaopro = int(input('1 - Adicionar notas' \
        '\n2 - Ver alunos'
        ''
        'opção: '))

        if funcaopro == 1:
            curso = int(input('selecione o curso:' \
            '\n1 - Desenvolvimento de Sistemas 1' \
            '\n2 - Enfermagem 1' \
            '\n3 - Administração 1' \
            '\n4 - Finanças 1' \
            '\n5 - Desenvolvimento de Sistemas 2' \
            '\n6 - Enfermagem 2' \
            '\n7 - Administração 2' \
            '\n8 - Finanças 2' \
            '\n9 - Desenvolvimento de Sistemas 3' \
            '\n10 - Enfermagem 3'))
            
            if curso == 1:
                print('curso: Desenvolvimento de sistemas 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 2:
                print('curso: Enfermagem 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 3:
                print('curso: Administração 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 4:
                print('curso: Finanças 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 5:
                print('curso: Desenvolvimento de sistemas 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 6:
                print('curso: Enfermagem 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 7:
                print('curso: Administração 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 8:
                print('curso: Finanças 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 9:
                print('curso: Desenvolvimento de sistemas 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 10:
                print('curso: Enfermagem 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

        if funcaopro == 2:
            print('Aluno 1' \
            '\nAluno 2' \
            '\n-------' \
            '\nAluno 40')

    if materia == 2:
        print('Muito bem! Bem vindo profesor(a)', nome)
        print('Aqui está o seu painel de controle na disciplina de matemática')

        print('Escolha oque quer fazer: ')
        funcaopro = int(input('1 - Adicionar notas' \
        '\n2 - Ver alunos'))

        if funcaopro == 1:
            curso = int(input('selecione o curso:' \
            '\n1 - Desenvolvimento de Sistemas 1' \
            '\n2 - Enfermagem 1' \
            '\n3 - Administração 1' \
            '\n4 - Finanças 1' \
            '\n5 - Desenvolvimento de Sistemas 2' \
            '\n6 - Enfermagem 2' \
            '\n7 - Administração 2' \
            '\n8 - Finanças 2' \
            '\n9 - Desenvolvimento de Sistemas 3' \
            '\n10 - Enfermagem 3'))
            
            if curso == 1:
                print('curso: Desenvolvimento de sistemas 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 2:
                print('curso: Enfermagem 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 3:
                print('curso: Administração 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 4:
                print('curso: Finanças 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 5:
                print('curso: Desenvolvimento de sistemas 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 6:
                print('curso: Enfermagem 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 7:
                print('curso: Administração 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 8:
                print('curso: Finanças 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 9:
                print('curso: Desenvolvimento de sistemas 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 10:
                print('curso: Enfermagem 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

        if funcaopro == 2:
            print('Aluno 1' \
            '\nAluno 2' \
            '\n-------' \
            '\nAluno 40')

    if materia == 3:
        print('Muito bem! Bem vindo profesor(a)', nome)
        print('Aqui está o seu painel de controle na disciplina de biologia')

        print('Escolha oque quer fazer: ')
        funcaopro = int(input('1 - Adicionar notas' \
        '\n2 - Ver alunos'))

        if funcaopro == 1:
            curso = int(input('selecione o curso:' \
            '\n1 - Desenvolvimento de Sistemas 1' \
            '\n2 - Enfermagem 1' \
            '\n3 - Administração 1' \
            '\n4 - Finanças 1' \
            '\n5 - Desenvolvimento de Sistemas 2' \
            '\n6 - Enfermagem 2' \
            '\n7 - Administração 2' \
            '\n8 - Finanças 2' \
            '\n9 - Desenvolvimento de Sistemas 3' \
            '\n10 - Enfermagem 3'))
            
            if curso == 1:
                print('curso: Desenvolvimento de sistemas 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 2:
                print('curso: Enfermagem 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 3:
                print('curso: Administração 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 4:
                print('curso: Finanças 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 5:
                print('curso: Desenvolvimento de sistemas 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 6:
                print('curso: Enfermagem 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 7:
                print('curso: Administração 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 8:
                print('curso: Finanças 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 9:
                print('curso: Desenvolvimento de sistemas 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 10:
                print('curso: Enfermagem 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

        if funcaopro == 2:
            print('Aluno 1' \
            '\nAluno 2' \
            '\n-------' \
            '\nAluno 40')

    if materia == 4:
        print('Muito bem! Bem vindo profesor(a)', nome)
        print('Aqui está o seu painel de controle na disciplina de filosofia')

        print('Escolha oque quer fazer: ')
        funcaopro = int(input('1 - Adicionar notas' \
        '\n2 - Ver alunos'))

        if funcaopro == 1:
            curso = int(input('selecione o curso:' \
            '\n1 - Desenvolvimento de Sistemas 1' \
            '\n2 - Enfermagem 1' \
            '\n3 - Administração 1' \
            '\n4 - Finanças 1' \
            '\n5 - Desenvolvimento de Sistemas 2' \
            '\n6 - Enfermagem 2' \
            '\n7 - Administração 2' \
            '\n8 - Finanças 2' \
            '\n9 - Desenvolvimento de Sistemas 3' \
            '\n10 - Enfermagem 3'))
            
            if curso == 1:
                print('curso: Desenvolvimento de sistemas 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 2:
                print('curso: Enfermagem 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 3:
                print('curso: Administração 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 4:
                print('curso: Finanças 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 5:
                print('curso: Desenvolvimento de sistemas 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 6:
                print('curso: Enfermagem 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 7:
                print('curso: Administração 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 8:
                print('curso: Finanças 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 9:
                print('curso: Desenvolvimento de sistemas 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 10:
                print('curso: Enfermagem 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

        if funcaopro == 2:
            print('Aluno 1' \
            '\nAluno 2' \
            '\n-------' \
            '\nAluno 40')

    if materia == 5:
        print('Muito bem! Bem vindo profesor(a)', nome)
        print('Aqui está o seu painel de controle na disciplina de fisica')

        print('Escolha oque quer fazer: ')
        funcaopro = int(input('1 - Adicionar notas' \
        '\n2 - Ver alunos'))

        if funcaopro == 1:
            curso = int(input('selecione o curso:' \
            '\n1 - Desenvolvimento de Sistemas 1' \
            '\n2 - Enfermagem 1' \
            '\n3 - Administração 1' \
            '\n4 - Finanças 1' \
            '\n5 - Desenvolvimento de Sistemas 2' \
            '\n6 - Enfermagem 2' \
            '\n7 - Administração 2' \
            '\n8 - Finanças 2' \
            '\n9 - Desenvolvimento de Sistemas 3' \
            '\n10 - Enfermagem 3'))
            
            if curso == 1:
                print('curso: Desenvolvimento de sistemas 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 2:
                print('curso: Enfermagem 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 3:
                print('curso: Administração 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 4:
                print('curso: Finanças 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 5:
                print('curso: Desenvolvimento de sistemas 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 6:
                print('curso: Enfermagem 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 7:
                print('curso: Administração 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 8:
                print('curso: Finanças 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 9:
                print('curso: Desenvolvimento de sistemas 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 10:
                print('curso: Enfermagem 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

        if funcaopro == 2:
            print('Aluno 1' \
            '\nAluno 2' \
            '\n-------' \
            '\nAluno 40')

    if materia == 6:
        print('Muito bem! Bem vindo profesor(a)', nome)
        print('Aqui está o seu painel de controle na disciplina de P.O.O')
        

        print('Escolha oque quer fazer: ')
        funcaopro = int(input('1 - Adicionar notas' \
        '\n2 - Ver alunos'))

        if funcaopro == 1:
            curso = int(input('\nselecione o curso:' \
            '\n1 - Desenvolvimento de Sistemas 2'))
            
            if curso == 1:
                print('curso: Desenvolvimento de sistemas 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

        if funcaopro == 2:
            print('Aluno 1' \
            '\nAluno 2' \
            '\n-------' \
            '\nAluno 40')

    if materia == 7:
        print('Muito bem! Bem vindo profesor(a)', nome)
        print('Aqui está o seu painel de controle na disciplina de ingles')
        

        print('Escolha oque quer fazer: ')
        funcaopro = int(input('1 - Adicionar notas' \
        '\n2 - Ver alunos'))

        if funcaopro == 1:
            curso = int(input('selecione o curso:' \
            '\n1 - Desenvolvimento de Sistemas 1' \
            '\n2 - Enfermagem 1' \
            '\n3 - Administração 1' \
            '\n4 - Finanças 1' \
            '\n5 - Desenvolvimento de Sistemas 2' \
            '\n6 - Enfermagem 2' \
            '\n7 - Administração 2' \
            '\n8 - Finanças 2' \
            '\n9 - Desenvolvimento de Sistemas 3' \
            '\n10 - Enfermagem 3'))
            
            if curso == 1:
                print('curso: Desenvolvimento de sistemas 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 2:
                print('curso: Enfermagem 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 3:
                print('curso: Administração 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 4:
                print('curso: Finanças 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 5:
                print('curso: Desenvolvimento de sistemas 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 6:
                print('curso: Enfermagem 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 7:
                print('curso: Administração 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 8:
                print('curso: Finanças 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 9:
                print('curso: Desenvolvimento de sistemas 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 10:
                print('curso: Enfermagem 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

        if funcaopro == 2:
            print('Aluno 1' \
            '\nAluno 2' \
            '\n-------' \
            '\nAluno 40')

    if materia == 8:
        print('Muito bem! Bem vindo profesor(a)', nome)
        print('Aqui está o seu painel de controle na disciplina de espanhol')

        print('Escolha oque quer fazer: ')
        funcaopro = int(input('1 - Adicionar notas' \
        '\n2 - Ver alunos'))

        if funcaopro == 1:
            curso = int(input('selecione o curso:' \
            '\n1 - Desenvolvimento de Sistemas 1' \
            '\n2 - Enfermagem 1' \
            '\n3 - Administração 1' \
            '\n4 - Finanças 1' \
            '\n5 - Desenvolvimento de Sistemas 2' \
            '\n6 - Enfermagem 2' \
            '\n7 - Administração 2' \
            '\n8 - Finanças 2' \
            '\n9 - Desenvolvimento de Sistemas 3' \
            '\n10 - Enfermagem 3'))
            
            if curso == 1:
                print('curso: Desenvolvimento de sistemas 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 2:
                print('curso: Enfermagem 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 3:
                print('curso: Administração 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 4:
                print('curso: Finanças 1')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 5:
                print('curso: Desenvolvimento de sistemas 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 6:
                print('curso: Enfermagem 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 7:
                print('curso: Administração 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 8:
                print('curso: Finanças 2')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 9:
                print('curso: Desenvolvimento de sistemas 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

            if curso == 10:
                print('curso: Enfermagem 3')
                nome = str(input('Digite o nome do aluno(a): '))
                nota = float(input('Digite a nota que deseja adicionar: '))
                print('nota', nota, 'para', nome, 'adiconada com sucesso!')
                if nota>10:
                    print('nota invalida')
                else:
                    print('nota', nota, 'para', nome, 'adiconada com sucesso!')

        if funcaopro == 2:
            print('Aluno 1' \
            '\nAluno 2' \
            '\n-------' \
            '\nAluno 40')

def gestor():

    print('-----MENU GESTOR-----\n')
    print('Escolha oque quer fazer: \n')
    funcaogestor = int(input('1 - Ver funcionários' \
    '\n2 - Realizar notificação' \
    ''))

    if funcaogestor == 1:

        print('-----COZINHEIROS-----\n')
        print('cozinheiro 1' \
        '\ncozinheiro 2' \
        '\ncozinheiro 3' \
        '\ncozinheiro 4')

        print('-----ZELADORES----\n')
        print('zelador 1' \
        '\nzelador 2' \
        '\nzelador 3' \
        '\nzelador 4\n')

        print('-----PORTEIROS----\n')
        print('Porteiro 1' \
        '\nPorteiro 2' \
        '\nPorteiro 3' \
        '\nPorteiro 4')

    if funcaogestor == 2:
        print('selecione a quem notificar: \n')
        notificar = int(input('1 - cozinheiros' \
        '\n2 - zeladores' \
        '\n3 - porteiros'))

        if notificar == 1:
            mensagem = str(input('digite a mensagem a ser enviada aos cozinheiros: '))
            print('a notificação: ', mensagem, 'foi enviada com sucesso!')

        if notificar == 2:
            mensagem = str(input('digite a mensagem a ser enviada aos zeladores: '))
            print('a notificação: ', mensagem, 'foi enviada com sucesso!')

        if notificar == 3:
            mensagem = str(input('digite a mensagem a ser enviada aos porteiros: '))
            print('a notificação: ', mensagem, 'foi enviada com sucesso!')

menu()

#git config --global user.email "ezequielbrandao001@gmail.com"
#git config --global user.name "ezequielbrandao99"