class concessionaria:
    def __init__(self, cliente = None, pagamento = None):
        self.cliente = cliente
        print('Bem vindo a concessionaria!')
        if cliente is None:
            self.cliente = input('Digite seu nome: ')
        print(f'Olá {self.cliente}, seja bem vindo!')

class veiculo:
    def __init__(self, categoria = None, marca = None, modelo = None, cor = None):
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

        if categoria is None:
            self.categoria = int(input('Digite a categoria do veiculo que deseja comprar (1 - carro/2 - moto/3 - consórcio): '))

            if self.categoria == 1:
                print('Legal saber que deseja comprar um carro!')

                class carro(veiculo):
                    def __init__(self, marca = None, modelo = None, cor = None):
                        marca = str(input('Voce tem preferencia de marca? '))

                        if marca == 'sim' or 'SIM':
                            print('Escolha qual marca prefere: ')
                            opcao = int(input('1 - Peugeot\n2 - Fiat\n3 - Chevrolet\n4 - Volkswagen\n'))
                            if opcao == 1:
                                self.marca = 'Peugeot'
                            elif opcao == 2:
                                self.marca = 'Fiat'
                            elif opcao == 3:
                                self.marca = 'Chevrolet'
                            elif opcao == 4:
                                self.marca = 'Volkswagen'
                            else:
                                print('opção inválida, escolha novamente')
                                exit()

                        self.modelo = str(input('Digite o modelo que deseja: '))
                        self.cor = str(input('Digite a cor que deseja: '))
                        print(f'Obrigado por escolher nossa concessionaria! Em breve entraremos em contato para a entrega de {self.marca} {self.modelo} {self.cor}.')

                        super().__init__(marca, modelo, cor)
                carro()
            if self.categoria == 2:
                print('Legal saber que deseja comprar uma moto!')

                class moto(veiculo):
                    def __init__(self, marca = None, modelo = None, cor = None):
                        marca = str(input('Voce tem preferencia de marca? '))

                        if marca == 'sim' or 'SIM':
                            print('escolha qual marca prefere: ')
                            opcao = int(input('1 - Honda\n2 - Yamaha\n3 - Suzuki\n4 - Kawasaki\n'))
                            if opcao == 1:
                                self.marca = 'Honda'
                            elif opcao == 2:
                                self.marca = 'Yamaha'
                            elif opcao == 3:
                                self.marca = 'Suzuki'
                            elif opcao == 4:
                                self.marca = 'Kawasaki'
                            else:
                                print('Opção inválida, escolha novamente')

                            self.modelo = str(input('Digite o modelo que deseja: '))
                            self.cor = str(input('Digite a cor que deseja: '))
                            print(f'Obrigado por escolher nossa concessionaria! Em breve entraremos em contato para a entrega de {self.marca} {self.modelo} {self.cor}.')

                        super().__init__(marca, modelo, cor)
                moto()            
            if self.categoria == 3:
                print('Legal saber que deseja fazer um consórcio!')

                class consorcio():
                    def __init__(self, pagamento = None):
                        self.pagamento = pagamento

                        if pagamento is None:
                            self.pagamento = int(input('Digite a forma de pagamento que deseja (1 - à vista/2 - parcelado): '))

                            if self.pagamento == 1:
                                valor_consorcio = float(input('Digite o valor total da carta de crédito que deseja: R$ ')) 
                                print('Obrigado por escolher nossa concessionaria! Em breve entraremos em contato para finalizar a compra à vista.')

                            elif self.pagamento == 2:
                                valor_consorcio = float(input('Digite o valor total do consórcio: R$ ')) 
                                parcelas = int(input('Digite em quantas vezes deseja parcelar: '))
                                valor_parcela = valor_consorcio / parcelas
                                print(f'Seu consórcio será parcelado em {parcelas}x de R$ {valor_parcela}')
                                print('Obrigado por escolher nossa concessionaria! Em breve entraremos em contato para finalizar a compra parcelada.')

                            else:
                                print('Opção inválida, escolha novamente')
                consorcio()
            exit()

concessionaria()
veiculo()