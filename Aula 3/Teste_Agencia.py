import unittest 
from dinheiro import Moeda
from banco import Banco 
from agencia import Agencia
from hamcrest import assert_that, equal_to


class TestAgencia(unittest.TestCase):

    def setUp(self):
        self.banco = Banco("BancoTeste", Moeda.BRL)
        self.agencia = Agencia("AgenciaTeste", 1, self.banco)

    def test_criar_conta(self):
        # Implicit Fixture Setup
        # Exercise SUT
        conta = self.agencia.criar_conta("Thomas")
        # Result Verification
        assert_that(conta.titular, equal_to("Thomas"))
        assert_that(conta.agencia, equal_to(self.agencia))
        # Fixture Teardown

    def test_buscar_conta(self):
        # Implicit + Inline Fixture Setup
        john = self.agencia.criar_conta("John")
        # Exercise SUT
        busca = self.agencia.obter_contas()
        # Result Verification
        assert_that(busca[0], equal_to(john))
        # Fixture Teardown

    def test_buscar_identificador(self):
        # Implicit Fixture Setup
        # Exercise SUT
        identificador = self.agencia.obter_identificador()
        # Result Verification
        assert_that(identificador, equal_to('001'))
        # Fixture Teardown