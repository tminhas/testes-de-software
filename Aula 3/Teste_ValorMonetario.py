import unittest
from dinheiro import Dinheiro, ValorMonetario, Moeda
from hamcrest import assert_that, equal_to, raises, calling


class TestValorMonetario(unittest.TestCase):

    def setUp(self):
        self.valor1 = ValorMonetario(Moeda.BRL, 300)
        self.valor2 = Dinheiro(Moeda.BRL, 0, 200)
        self.valor_diferente = ValorMonetario(Moeda.USD, 200)

    def test_subtrair_valores(self):
        # Implicit Fixture Setup
        # Exercise SUT
        resultado = self.valor1.subtrair(self.valor2)
        # Result Verification
        assert_that(resultado.obter_quantia().obter_quantia_em_escala(), equal_to(100))
        # Fixture Teardown

    def test_somar_valores(self):
        # Implicit Fixture Setup
        # Exercise SUT
        resultado = self.valor1.somar(self.valor2)
        # Result Verification
        assert_that(resultado.obter_quantia().obter_quantia_em_escala(), equal_to(500))

    def test_somar_valores_com_moedas_diferentes(self):
        # Implicit Fixture Setup
        # Exercise SUT & Result Verification
        assert_that(calling(self.valor1.somar).with_args(self.valor_diferente), raises(Exception))

    def test_subtrair_valores_com_moedas_diferentes(self):
        # Implicit Fixture Setup
        # Exercise SUT & Result Verification
        assert_that(calling(self.valor1.subtrair).with_args(self.valor_diferente), raises(Exception))

    def test_igual_a_zero(self):
        # Inline Fixture Setup
        valor = ValorMonetario(Moeda.BRL)
        # Exercise SUT
        zero = valor.zero()
        # Result Verification
        assert_that(zero, equal_to(True))
        # Fixture Teardown