class Pessoa:
    def __init__(self, cpf, nome, idade, telefone):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __repr__(self):
        return repr(f'NOME:{self.nome} CPF:{self.cpf} IDADE:{self.idade} TELEFONE:{self.telefone}')

    def createDict(self):

        return {'cpf': self.cpf, 'nome': self.nome, 'idade': self.idade,'telefone': self.telefone}

#criar metodo para criar dict com os dados do objeto pessoa