def estacionamento():
    print('\nNo estacionamento tem as seguintes marcas e modelos: ')

def Volkswagen():
    print('Volkswagen: o Fox é o melhor custo benefício.')

def Chevrolet():
    print('Chevrolet: Onix novo não presta...')

def Fiat():
    print('Fiat Toro é a masi vendida do segmento.')

def RAM():
    print('A RAM 700 tem a mesma plataforma da Fiat Toro e muda apenas o nome.')

def Jetta():
    print('O Jetta GLI tem o mesmo motor do AUDI A4. O famoso 2.0 TFSI.')

estacionamento()
Volkswagen()
Chevrolet()
Fiat()
RAM()
Jetta()

escolha = int(input('\nDigite a marca que deseja ver os modelos:\n' \
'1 - Mercedes\n' \
'2 - BMW\n' \
'3 - Porsche\n' \
'4 - Audi'))

if(escolha == 1):
    print('\nC180\nCLK\nAMG GTR\nA200')

if(escolha == 2):
    print('\nM3\nM4\n320i\nI8')

if(escolha == 3):
    print('\nBoxter S\nTycan \n911 carrera\nGT3 RS')

if(escolha == 4):
    print('\nA3\nA4\nR8\nRS6')