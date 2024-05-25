import unittest

from invalid_repeated_employee import InvalidRepeatedEmployee
from empresa import Empresa
from funcionario import Funcionario
from projeto import Projeto
from invalid_cpf_format import InvalidCpfFormat
from invalid_repeated_project import InvalidRepeatedProject

class TestsTDD(unittest.TestCase):
    def setUp(self):
        self.reivax = Empresa('REIVAX')
        self.roberto = Funcionario('Roberto', 31, '529.982.247-25')
        self.rafael = Funcionario('Rafael', 24, '529.982.243-25')

    def test_1_cria_empresa(self):
        reivax = Empresa('REIVAX')
        self.assertEqual('REIVAX', reivax.nome)

    def test_2_cria_funcionario(self):
        thomas = Funcionario('Thomás', 24, "012.345.678-90")
        self.assertEqual('Thomás', thomas.nome)
        self.assertEqual(24, thomas.idade)

    def test_3_cria_projeto(self):
        thomas = Funcionario('Thomás', 24, "111.444.777-35")
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
        joao = self.reivax.contrata_funcionario('Joao', 28, "987.654.321-00")
        self.assertIn(joao, self.reivax.funcionarios)

    def test_8_empresa_lista_funcionarios(self):
        pedro = self.reivax.contrata_funcionario('Pedro', 29, "123.456.789-09")
        assaleh = self.reivax.contrata_funcionario('Assaleh', 93, "123.456.722-08")
        funcionarios = self.reivax.lista_funcionarios()
        self.assertIn(pedro, funcionarios)
        self.assertIn(assaleh, funcionarios)

    def test_9_cria_projeto_sem_funcionarios(self):
        mecanico = self.reivax.cria_projeto('mecanico')
        self.assertEqual('mecanico', mecanico.nome)

    def test_10_contrata_dois_funcionarios_iguai(self):
        self.reivax.contrata_funcionario('Lucas', 20, "123.456.789-10")
        with self.assertRaises(InvalidRepeatedEmployee):
            self.reivax.contrata_funcionario('Lucas', 20, "123.456.789-10")

    def test_11_retorna_o_cpf_do_funcionario(self):
        self.assertEqual(self.roberto.retorna_o_cpf_do_funcionario(), '529.982.247-25')

    def test_12_retorna_o_id_do_funcionario(self):
        self.assertEqual(self.roberto.retorna_o_id_do_funcionario(), 6)

    def test_13_cria_funcionario_com_cpf_invalido(self):
        with self.assertRaises(InvalidCpfFormat):
            Funcionario('Rafael', '52', '1234151')

    def test_14_cria_dois_projetos(self):
        mecanico = self.reivax.cria_projeto('mecanico')
        solar = self.reivax.cria_projeto('solar')
        self.assertEqual('mecanico', mecanico.nome)
        self.assertEqual('solar', solar.nome)
        self.assertIn(mecanico, self.reivax.projetos)
        self.assertIn(solar, self.reivax.projetos)
    
    def test_15_cria_dois_projetos_iguais(self):
        self.reivax.cria_projeto('mecanico')
        with self.assertRaises(InvalidRepeatedProject):
            self.reivax.cria_projeto('mecanico')
        

if __name__ == '__main__':
    unittest.main()
