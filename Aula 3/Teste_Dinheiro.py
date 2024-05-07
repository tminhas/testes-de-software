import unittest 
from dinheiro import Dinheiro, Moeda
from hamcrest import assert_that, equal_to, raises


class TestDinheiro(unittest.TestCase):

    def test_criar_dinheiro_negativo(self):
        # Fixture Setup
        # Exercise SUT
        # Result Verification
        assert_that(lambda: Dinheiro(Moeda.BRL, -3, -4), raises(ValueError))
        # Fixture Teardown

    def test_criar_dinheiro_em_escala(self):
        # Inline Fixture Setup
        vinte_reais_30_cents = Dinheiro(Moeda.BRL, 20, 30)
        # Exercise SUT
        escala = vinte_reais_30_cents.obter_quantia_em_escala()
        # Result Verification
        assert_that(escala, equal_to(2030))
        # Fixture Teardown

    def test_criar_dinheiro_com_string(self):
        # Inline Fixture Setup
        # Exercise SUT
        # Result Verification
        assert_that(lambda: Dinheiro(Moeda.BRL, "3", "4"), raises(TypeError))
        # Fixture Teardown