from typing import List

from src.db.database import Database
from src.models.pessoa import Pessoa


class PessoaManager:
    database: Database
    pessoas: List[Pessoa]

    def __init__(self):
        self.database = Database()
        self.pessoas = Database.ler_pessoas()


    def criar_pessoa(self, cpf, nome, idade, telefone):

        nova_pessoa = Pessoa(cpf=cpf, nome=nome, idade=idade, telefone=telefone)
        self.pessoas.append(nova_pessoa)

        self.database.gravar_pessoas(self.pessoas)

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

        self.database.gravar_pessoas(self.pessoas)

        return pessoa

    def excluir_pessoa(self, cpf):

        pessoa = self.buscar_pessoa(cpf)
        self.pessoas.remove(pessoa)

        self.database.gravar_pessoas(self.pessoas)



