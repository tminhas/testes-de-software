import re
from src.invalid_cpf_format import InvalidCpfFormat


class Funcionario:
    _id_count = 0

    def __init__(self, nome, idade, cpf):
        type(self)._id_count += 1
        self.__id = type(self)._id_count
        self.nome = nome
        self.idade = idade
        if not self.__verificar_formatacao_cpf(cpf):
            raise InvalidCpfFormat
        self.__cpf = cpf

    @staticmethod
    def __verificar_formatacao_cpf(cpf):
        # Expressão regular para o formato XXX.XXX.XXX-YY
        padrao = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

        # Verifica se a string corresponde ao padrão
        if padrao.match(cpf):
            return True
        else:
            return False

    def retorna_o_id_do_funcionario(self):
        return self.__id

    def retorna_o_cpf_do_funcionario(self):
        return self.__cpf
