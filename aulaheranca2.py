class veiculo:
    def __init__(self, modelo = None, ano = None, placa = None, marca = None):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.marca = marca
    
class introducao:
        
    print('\nBem vindo ao sistema de verificação de IPVA')
    escolha = int(input('''Para comerçarmos, digite: 
                        1 - IPVA -> carro
                        2 - IPVA ->  moto'''))
    
    if escolha == 1:

        class carro(veiculo):

            def __init__(self, modelo=None, ano=None, placa=None, marca=None):

                if marca is None:
                    marca = input('Digite a marca do carro: ')

                if modelo is None:
                    modelo = input('Digite o modelo do carro: ')

                if ano is None:
                    ano = input('Digite o ano do carro: ')

                if placa is None:
                    placa = input('Digite a placa do carro: ')

                super().__init__(modelo, ano, placa, marca)
                
        carro()

        print('<------------------------------------------->')

    if escolha == 2:

        class moto(veiculo):

            def __init__(self, modelo=None, ano=None, placa=None, marca=None):

                if marca is None:
                    marca = input('\nDigite a marca da moto: ')

                if modelo is None:
                    modelo = input('Digite o modelo da moto: ')

                if ano is None:
                    ano = input('Digite o ano da moto: ')

                if placa is None:
                    placa = input('Digite a placa da moto: ')

                print('<------------------------------------------->')

                super().__init__(modelo, ano, placa, marca)

        moto()

introducao()

print('A verificação será realizada e você será notificado em instantes...')