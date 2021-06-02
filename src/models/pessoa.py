class Pessoa:
    def __init__(self, cpf, nome, idade, telefone):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __repr__(self):
        return repr(f'NOME:{self.nome} CPF:{self.cpf} IDADE:{self.idade} TELEFONE:{self.telefone}')