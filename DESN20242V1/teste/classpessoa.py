class Pessoa:
    def __init__(self, idade, nome, peso, altura):
        self.idade = idade
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def emagrecer(self, quantidade):
        self.peso -= quantidade  # para dimunuir o peso

    def engordar(self, quantidade):
        self.peso += quantidade  # para aumentar o peso

    def envelhecer(self, anos):
        self.idade += anos  # para aumentar a idade

    def crescer(self):
        if self.idade <= 21:
            self.altura += 1  # Aumentar a altura de forma pequena

# Criar uma pessoa
pessoa1 = Pessoa(17, "Giuseppe Cadura", 80, 1.87)

# Mostrar os dados da pessoa
print(pessoa1.idade)
print(pessoa1.nome)
print(pessoa1.peso)
print(pessoa1.altura)


pessoa1.crescer()     # Aumenta a altura

# Mostrar os dados depois da mudança
print(f"Idade: {pessoa1.idade}")
print(f"Nome: {pessoa1.nome}")
print(f"Peso: {pessoa1.peso}")
print(f"Altura: {pessoa1.altura}")




