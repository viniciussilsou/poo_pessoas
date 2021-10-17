from typing import List

from src.managers.json_manager import JsonManager
from src.models.pessoa import Pessoa


class Database:
    pessoas_db_path: str = 'db/pessoas_db.json'

    def __init__(self):
        pass

    @staticmethod
    def ler_pessoas() -> List[Pessoa]:
        pessoas_from_json: list = JsonManager.read_json(Database.pessoas_db_path)

        pessoas: List[Pessoa] = list()

        for pessoa_from_json in pessoas_from_json:
            nova_pessoa = Pessoa(
                cpf=pessoa_from_json.get("cpf"),
                nome=pessoa_from_json.get("nome"),
                idade=pessoa_from_json.get("idade"),
                telefone=pessoa_from_json.get("telefone"),
            )
            pessoas.append(nova_pessoa)

        return pessoas


    def gravar_pessoas(self, pessoas: List[Pessoa]):
        pessoas_to_json: List[dict] = list()

        for pessoa in pessoas:
            pessoas_to_json.append({
                "cpf": pessoa.cpf,
                "nome": pessoa.nome,
                "idade": pessoa.idade,
                "telefone":pessoa.telefone,

            })

        JsonManager.write_json(pessoas_to_json, self.pessoas_db_path)