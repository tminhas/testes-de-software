class Projeto:
    def __init__(self, nome, funcionarios):
        self.funcionarios = funcionarios
        self.nome = nome

    def adiciona_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
