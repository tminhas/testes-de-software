import unittest 
from dinheiro import Dinheiro, Moeda


class TestDinheiro(unittest.TestCase):

	def test_criar_dinheiro_negativo(self):
		# Fixture Setup
		# Exercise SUT
		with self.assertRaises(ValueError):
			dinheiro_negativo = Dinheiro(Moeda.BRL, -3, -4)
		# Result Verification
		# Fixture Teardown

	def test_criar_dinheiro_em_escala(self):
		# Inline Fixture Setup
		vinte_reais_30_cents = Dinheiro(Moeda.BRL, 20, 30)
		# Exercise SUT
		escala = vinte_reais_30_cents.obter_quantia_em_escala()
		# Result Verification
		self.assertEqual(2030, escala)
		# Fixture Teardown

	def test_criar_dinheiro_com_string(self):
		# Inline Fixture Setup
		# Exercise SUT
		with self.assertRaises(TypeError):
			dinheiro_invalido = Dinheiro(Moeda.BRL, "3", "4")
		# Result Verification
		# Fixture Teardown