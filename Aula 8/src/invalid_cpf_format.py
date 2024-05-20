

class InvalidCpfFormat(Exception):

    def __init__(self):
        self.message = 'Cpf do funcionario não existe.'
        # super().__init__(self.message)