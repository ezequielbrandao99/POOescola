class Pessoa:
    def __init__(self, nome, idade):
        # Atributo privado/fortemente protegido por convenção
        # Python faz uma "mudança de nome" (name mangling) aqui
        self.__nome = nome
        self.__idade = idade # <- Este atributo é "encapsulado"

    # Método Público: Getter (para obter o valor)
    def get_idade(self):
        """Retorna a idade."""
        return self.__idade

    # Método Público: Setter (para modificar o valor de forma controlada)
    def set_idade(self, nova_idade):
        """Define uma nova idade, aplicando uma regra de negócio."""
        
        # O encapsulamento permite que a CLASSE decida como o dado será modificado
        if 0 < nova_idade <= 120:
            self.__idade = nova_idade
            print(f"Idade de {self.__nome} alterada para {self.__idade}.")
        else:
            print("Erro: Idade inválida. A alteração foi bloqueada.")

# Cria o objeto
p = Pessoa("Maria", 30)

## Acesso Controlado (Correto):

# 1. Obter a idade usando o método GETTER
idade_atual = p.get_idade()
print(f"Idade atual (Getter): {idade_atual}")
# Saída: Idade atual (Getter): 30

# 2. Modificar a idade usando o método SETTER (Sucesso)
p.set_idade(35)
# Saída: Idade de Maria alterada para 35.

# 3. Modificar a idade usando o método SETTER (Falha na regra de negócio)
p.set_idade(200) 
# Saída: Erro: Idade inválida. A alteração foi bloqueada.

print("-" * 30)

## Acesso Direto (Desencorajado em Python, mas tecnicamente possível):

# Embora seja privado, Python NÃO PROÍBE, apenas dificulta (Convenção)
# Se você tentar acessar diretamente, dará um erro (AttributeError)
try:
    print(f"Tentando acessar diretamente: {p.__idade}")
except AttributeError as e:
    print(f" Erro ao tentar acessar diretamente: {e}") 
    # Saída: Erro ao tentar acessar diretamente: 'Pessoa' object has no attribute '__idade'