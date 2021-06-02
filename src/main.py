from src.managers.pessoa_manager import PessoaManager

cpf = 40386811814
nome = 'Vinicius'
idade = 28
telefone = 993319440

pessoa_manager = PessoaManager()
nova_pessoa = pessoa_manager.criar_pessoa(cpf, nome, idade, telefone)

pessoa_buscada = pessoa_manager.buscar_pessoa(cpf)

pessoa_alterar = pessoa_manager.atualizar_pessoa(cpf, "fulano", 50, 343444343)
pessoa_buscada = pessoa_manager.buscar_pessoa(cpf)

nova_pessoa = pessoa_manager.criar_pessoa(3344433434, "teste", 56, 355546667)
deletar_pessoa = pessoa_manager.excluir_pessoa(40386811814)


lista = pessoa_manager.buscar_pessoa()
print(lista)



