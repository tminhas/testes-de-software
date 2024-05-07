import unittest 
from dinheiro import Moeda
from banco import Banco 
from agencia import Agencia


class TestAgencia(unittest.TestCase):

	def setUp(self):
		self.banco = Banco("BancoTeste", Moeda.BRL)
		self.agencia = Agencia("AgenciaTeste", 1, self.banco)

	def test_criar_conta(self):
		# Implicit Fixture Setup
		# Exercise SUT
		conta = self.agencia.criar_conta("Thomas")
		# Result Verification
		self.assertEqual("Thomas", conta.titular)
		self.assertEqual(self.agencia, conta.agencia)
		# Fixture Teardown

	def test_buscar_conta(self):
		# Implicit + Inline Fixture Setup
		john = self.agencia.criar_conta("John")
		# Exercise SUT
		busca = self.agencia.obter_contas()
		# Result Verification
		self.assertEqual(john, busca[0])
		# FIxture Teardown
  
	def test_buscar_identificador(self):
		# Implicit Fixture Setup
		# Exercise SUT
		identificador = self.agencia.obter_identificador()
		# Result Verification
		self.assertEqual('001', identificador)
		# Fixture Teardown
  