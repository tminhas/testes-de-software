import unittest 
from dinheiro import Moeda, Dinheiro, ValorMonetario
from transacao import TransacaoNaoRealizada, Entrada


class TestTransacao(unittest.TestCase):

    def test_transacao_nao_realizada(self):
        # Inline Fixture Setup
        transacao_base = Entrada(Dinheiro(Moeda.BRL, 100, 0))
        transacao_nao_realizada = TransacaoNaoRealizada(transacao_base)
        saldo = ValorMonetario(Moeda.BRL, 500)
        # Exercise SUT
        saldo_final = transacao_nao_realizada.contabilizar(saldo)
        # Result Verification
        self.assertEqual(saldo_final, saldo)
        # Fixture Teardown
