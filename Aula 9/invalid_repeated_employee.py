
class InvalidRepeatedEmployee(Exception):

    def __init__(self):
        self.message = 'Funcionario duplicado.'
        # super().__init__(self.message)