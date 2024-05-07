import unittest 
from dinheiro import Moeda
from banco import Banco 
from agencia import Agencia
from hamcrest import assert_that, equal_to


class TestBanco(unittest.TestCase):
    
    def setUp(self):
        self.banco = Banco("BancoTeste", Moeda.BRL)
  
    def test_criar_agencia(self):
        # Fixture Setup
        # Exercise SUT
        agencia = Agencia("AgenciaTeste3", 3, self.banco)
        # Result Verification
        assert_that(agencia.nome, equal_to("AgenciaTeste3"))
        assert_that(agencia.banco, equal_to(self.banco))
        # Fixture Teardown

    def test_multiplas_agencias(self):
        # Fixture Setup
        self.banco.criar_agencia("AgenciaTeste1")
        self.banco.criar_agencia("AgenciaTeste2")
        # Exercise SUT
        agencias = self.banco.obter_agencias()
        # Result Verification
        assert_that(len(agencias), equal_to(2))
        # Fixture Teardown
