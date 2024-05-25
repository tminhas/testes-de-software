class Ocorrencia:
    id = 0
    def __init__(self, nome, prioridade, funcionario):
        self.nome = nome
        self.status = 1 # 1 Aberta 0 Fechada
        self.prioridade = prioridade
        self.funcionario = funcionario
        Ocorrencia.id += 1
        self.id = Ocorrencia.id

    def fecha_ocorrencia(self):
        self.status = 0 
        self.funcionario.ocorrencias -= 1

    