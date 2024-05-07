import unittest 
from dinheiro import Moeda
from banco import Banco 
from agencia import Agencia


class TestBanco(unittest.TestCase):
    
	def setUp(self):
		self.banco = Banco("BancoTeste", Moeda.BRL)
  
	def test_criar_agencia(self):
		# Implicit Fixture Setup
		# Exercise SUT
		agencia = Agencia("AgenciaTeste3", 3, self.banco)
		# Result Verification
		self.assertEqual("AgenciaTeste3", agencia.nome)
		self.assertEqual(self.banco, agencia.banco)
		# Fixture Teardown

	def test_multiplas_agencias(self):
		# Implicit + Inline Fixture Setup
		self.banco.criar_agencia("AgenciaTeste1")
		self.banco.criar_agencia("AegnciaTeste2")
		# Exercise SUT
		agencias = self.banco.obter_agencias()
		# Result Verification
		self.assertEqual(2, len(agencias))
		# Fixture Teardown
