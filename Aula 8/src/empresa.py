from src.projeto import Projeto
from src.funcionario import Funcionario
from src.invalid_repeated_employee import InvalidRepeatedEmployee
from src.invalid_repeated_project import InvalidRepeatedProject

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.projetos = []
        self.funcionarios = []

    def cria_projeto(self, nome, funcionarios=None):
        if funcionarios is None:
            funcionarios = []
        if any(projeto_nome.nome == nome for projeto_nome in self.projetos):
            raise InvalidRepeatedProject
        else:
            projeto = Projeto(nome, funcionarios)
            self.projetos.append(projeto)
            return projeto

    def contrata_funcionario(self, nome, idade, cpf):
        if any(funcionario_obj.retorna_o_cpf_do_funcionario() == cpf for funcionario_obj in self.funcionarios):
            raise InvalidRepeatedEmployee

        else:
            funciorio = Funcionario(nome, idade, cpf)
            self.funcionarios.append(funciorio)
            return funciorio

    def lista_funcionarios(self):
        return self.funcionarios
