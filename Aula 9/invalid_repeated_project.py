
class InvalidRepeatedProject(Exception):

    def __init__(self):
        self.message = 'Projeto duplicado.'
        # super().__init__(self.message)