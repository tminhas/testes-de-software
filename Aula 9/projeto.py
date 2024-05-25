from ocorrencia import Ocorrencia
from funcionario import Funcionario


class Projeto:
    def __init__(self, nome, funcionarios):
        self.funcionarios = funcionarios
        self.nome = nome
        self.ocorrencias = []

    def adiciona_funcionario(self, funcionario=Funcionario):
        self.funcionarios.append(funcionario)

    def cria_ocorrencia(self, nome, prioridade, funcionario=Funcionario):
        if funcionario.ocorrencias >= 10:
            raise Exception("Funcionário já possui 10 ocorrências abertas.")
        ocorrencia = Ocorrencia(nome, prioridade, funcionario)
        self.ocorrencias.append(ocorrencia)
        funcionario.ocorrencias += 1

        return ocorrencia

        
