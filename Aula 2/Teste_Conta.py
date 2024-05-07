import unittest 
from dinheiro import Moeda, ValorMonetario
from banco import Banco 
from agencia import Agencia


class TestConta(unittest.TestCase):

	def setUp(self):
		self.banco = Banco("BancoTeste", Moeda.BRL)
		self.agencia = Agencia("AgenciaTeste", 1, self.banco)
		self.conta = self.agencia.criar_conta("Thomas")

	def test_calcular_saldo(self):
		# Implicit + Inline Fixture Setup
		valor = ValorMonetario(Moeda.BRL)
		zero = valor.obter_quantia()
		# Exercise SUT
		saldo = self.conta.calcular_saldo()
		# Result Verification
		self.assertEqual(zero, saldo)
		# Fixture Teardown
  