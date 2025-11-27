class perfil:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    @property
    def email(self):
        return self.__email
    
    email.setter
    def email(self, novo_email = None):

        self.email = email
        if novo_email is None:
            email = str(input("Digite o novo email: "))

            print('Email cadastrado: ', email)

perfil.email = perfil
print('Email cadastrado: ', perfil.email)