import unittest

from src.empresa import Empresa
from src.funcionario import Funcionario
from src.projeto import Projeto


class TestsTDD(unittest.TestCase):
    def setUp(self):
        self.reivax = Empresa('REIVAX')
        self.roberto = Funcionario('Roberto', 31)
        self.rafael = Funcionario('Rafael', 24)

    def test_1_cria_empresa(self):
        reivax = Empresa('REIVAX')
        self.assertEqual('REIVAX', reivax.nome)

    def test_2_cria_funcionario(self):
        thomas = Funcionario('Thomás', 24)
        self.assertEqual('Thomás', thomas.nome)
        self.assertEqual(24, thomas.idade)

    def test_3_cria_projeto(self):
        thomas = Funcionario('Thomás', 24)
        software = Projeto('Agus', [thomas])
        self.assertEqual('Agus', software.nome)
        self.assertEqual('Thomás', software.funcionarios[0].nome)

    def test_4_adiciona_funcionario_em_projeto(self):
        eletrico = Projeto('Rayner', [])
        eletrico.adiciona_funcionario(self.roberto)
        self.assertEqual('Roberto', eletrico.funcionarios[0].nome)

    def test_5_cria_projeto_em_empresa(self):
        matanzas = self.reivax.cria_projeto('Matanzas', [])
        self.assertEqual('Matanzas', matanzas.nome)
        self.assertIn(matanzas, self.reivax.projetos)

    def test_6_adiciona_funcionarios_em_projeto(self):
        solar = Projeto('Solar', [])
        solar.adiciona_funcionario(self.roberto)
        solar.adiciona_funcionario(self.rafael)
        self.assertEqual(2, len(solar.funcionarios))
        self.assertEqual(self.roberto, solar.funcionarios[0])
        self.assertEqual(self.rafael, solar.funcionarios[1])

    def test_7_contrata_funcionario(self):
        joao = self.reivax.contrata_funcionario('Joao', 28)
        self.assertIn(joao, self.reivax.funcionarios)

    def test_8_empresa_lista_funcionarios(self):
        pedro = self.reivax.contrata_funcionario('Pedro', 29)
        assaleh = self.reivax.contrata_funcionario('Assaleh', 93)
        funcionarios = self.reivax.lista_funcionarios()
        self.assertIn(pedro, funcionarios)
        self.assertIn(assaleh, funcionarios)

    def test_9_cria_projeto_sem_funcionarios(self):
        mecanico = self.reivax.cria_projeto('mecanico')
        self.assertEqual('mecanico', mecanico.nome)


if __name__ == '__main__':
    unittest.main()
