import unittest 
from dinheiro import Moeda, Dinheiro, ValorMonetario
from transacao import TransacaoNaoRealizada, Entrada
from hamcrest import assert_that, equal_to


class TestTransacao(unittest.TestCase):

    def test_transacao_nao_realizada(self):
        # Inline Fixture Setup
        transacao_base = Entrada(Dinheiro(Moeda.BRL, 100, 0))
        transacao_nao_realizada = TransacaoNaoRealizada(transacao_base)
        saldo = ValorMonetario(Moeda.BRL, 500)
        # Exercise SUT
        saldo_final = transacao_nao_realizada.contabilizar(saldo)
        # Result Verification
        assert_that(saldo_final, equal_to(saldo))
        # Fixture Teardown