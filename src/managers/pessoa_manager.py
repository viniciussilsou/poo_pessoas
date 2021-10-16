from src.models.pessoa import Pessoa


class PessoaManager:
    def __init__(self):
        self.pessoas = list()

#criar obj em json e manipular o json
#converter obj pessoa em dict
#escolher como salvar json e csv
#criar classe pra manipular(ler/gravar) JSON e Csv



    def criar_pessoa(self, cpf, nome, idade, telefone):

        nova_pessoa = Pessoa(cpf=cpf, nome=nome, idade=idade, telefone=telefone)
        self.pessoas.append(nova_pessoa)

        return nova_pessoa

    def buscar_pessoa(self, cpf=None):

        if cpf is None:
            return self.pessoas

        for pessoa in self.pessoas:
            if cpf == pessoa.cpf:
                return pessoa

    def atualizar_pessoa(self, cpf, nome, idade, telefone):

        pessoa = self.buscar_pessoa(cpf)
        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.telefone = telefone

        return pessoa

    def excluir_pessoa(self, cpf):

        pessoa = self.buscar_pessoa(cpf)
        self.pessoas.remove(pessoa)

    def createDict(self):

        return {'cpf': Pessoa.cpf, 'nome': self.nome, 'idade': self.idade, 'telefone': self.telefone}

