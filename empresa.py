from projeto import Projeto
from funcionario import Funcionario


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.projetos = []
        self.funcionarios = []

    def cria_projeto(self, nome, funcionarios=None):
        if funcionarios is None:
            funcionarios = []
        projeto = Projeto(nome, funcionarios)
        self.projetos.append(projeto)
        return projeto

    def contrata_funcionario(self, nome, idade):
        funcionario = Funcionario(nome, idade)
        self.funcionarios.append(funcionario)
        return funcionario

    def lista_funcionarios(self):
        return self.funcionarios
