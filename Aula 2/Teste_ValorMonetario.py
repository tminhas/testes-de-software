import unittest
from dinheiro import Dinheiro, ValorMonetario, Moeda


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
		self.assertEqual(resultado.obter_quantia().obter_quantia_em_escala(), 100)
		# Fixture Teardown

	def test_somar_valores(self):
		# Implicit Fixture Setup
		# Exercise SUT
		resultado = self.valor1.somar(self.valor2)
		# Result Verification
		self.assertEqual(resultado.obter_quantia().obter_quantia_em_escala(), 500)

	def test_somar_valores_com_moedas_diferentes(self):
		# Implicit Fixture Setup
		# Exercise SUT
		with self.assertRaises(Exception):
			resultado = self.valor1.somar(self.valor_diferente)
		# Result Verification
		# Fixture Teardown

	def test_subtrair_valores_com_moedas_diferentes(self):
		# Implicit Fixture Setup
		# Exercise SUT
		with self.assertRaises(Exception):
			resultado = self.valor1.subtrair(self.valor_diferente)
		# Result Verification
		# Fixture Teardown

	def test_igual_a_zero(self):
		# Inline Fixture Setup
		valor = ValorMonetario(Moeda.BRL)
		# Exercise SUT
		zero = valor.zero()
		# Result Verification
		self.assertTrue(zero)
		# Fixture Teardown