import unittest 
from dinheiro import Moeda, Dinheiro, ValorMonetario
from sistema_bancario import SistemaBancario
from operacao import EstadosDeOperacao


class TestHelper:

	def criar_sistema_bancario_com_banco():
		sistema = SistemaBancario()
		banco = sistema.criar_banco("Banco Teste", Moeda.BRL)
		return sistema, banco
	
	def criar_conta_em_banco(banco, usuario):
		agencia = banco.criar_agencia("Agencia")
		conta = agencia.criar_conta(usuario)
		return conta
		

class TestSistemaBancario(unittest.TestCase):

	def test_criar_banco(self):
		# Fixture Setup
		sistema = SistemaBancario()
		# Exercise SUT
		banco = sistema.criar_banco("Banco Teste", Moeda.BRL)
		# Result Verification
		self.assertIsNotNone(banco)
		self.assertEqual(banco.nome, "Banco Teste")
		self.assertEqual(banco.moeda, Moeda.BRL)

	def test_obter_banco_inexistente(self):
		# Fixture Setup
		sistema = SistemaBancario()
		# Exercise SUT
		banco_obtido = sistema.obter_banco("Banco Teste")
		# Result Verification
		self.assertIsNone(banco_obtido)
		# Fixture Teardown

	def test_obter_banco(self):
		# Delegated Fixture Setup
		sistema, banco = TestHelper.criar_sistema_bancario_com_banco()
		# Exercise SUT
		banco_obtido = sistema.obter_banco("Banco Teste")
		# Result Verification
		self.assertIsNotNone(banco_obtido)
		self.assertEqual(banco_obtido, banco)
		# Fixture Teardown

	def test_depositar(self):
		# Delegated + Inline Fixture Setup
		sistema, banco = TestHelper.criar_sistema_bancario_com_banco()
		conta = TestHelper.criar_conta_em_banco(banco, "Thomas")
		quantia_deposito = Dinheiro(Moeda.BRL, 100, 0)
		# Exercise SUT
		operacao = sistema.depositar(conta, quantia_deposito)
		# Result Verification
		self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
		self.assertEqual(conta.calcular_saldo(), ValorMonetario(Moeda.BRL, 10000))
		# Fixture Teardown

	def test_sacar(self):
		# Delegated + Inline Fixture Setup
		sistema, banco = TestHelper.criar_sistema_bancario_com_banco()
		conta = TestHelper.criar_conta_em_banco(banco, "Thomas")
		quantia_deposito = Dinheiro(Moeda.BRL, 100, 0)
		sistema.depositar(conta, quantia_deposito)
		quantia_saque = Dinheiro(Moeda.BRL, 50, 0)
		# Exercise SUT
		operacao = sistema.sacar(conta, quantia_saque)
		# Result Verification
		self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
		self.assertEqual(conta.calcular_saldo(), ValorMonetario(Moeda.BRL, 5000))
		# Fixture Teardown

	def test_transferir(self):
		# Delegated + Inline Fixture Setup
		sistema, banco = TestHelper.criar_sistema_bancario_com_banco()
		conta_origem = TestHelper.criar_conta_em_banco(banco, "Thomas")
		conta_destino = TestHelper.criar_conta_em_banco(banco, "Rafael")
		quantia_deposito = Dinheiro(Moeda.BRL, 100, 0)
		sistema.depositar(conta_origem, quantia_deposito)
		quantia_transferencia = Dinheiro(Moeda.BRL, 50, 0)
		# Exercise SUT
		operacao = sistema.transferir(conta_origem, conta_destino, quantia_transferencia)
		# Result Verification
		self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
		self.assertEqual(conta_origem.calcular_saldo(), ValorMonetario(Moeda.BRL, 5000))
		self.assertEqual(conta_destino.calcular_saldo(), ValorMonetario(Moeda.BRL, 5000))
		# Fixture Teardown

	def test_transferir_moeda_invalida(self):
		# Delegated + Inline Fixture Setup
		sistema, banco = TestHelper.criar_sistema_bancario_com_banco()
		conta_origem = TestHelper.criar_conta_em_banco(banco, "Thomas")
		conta_destino = TestHelper.criar_conta_em_banco(banco, "Rafael")
		valor_origem = Dinheiro(Moeda.BRL, 100, 0)
		sistema.depositar(conta_origem, valor_origem)
		valor_destino = Dinheiro(Moeda.USD, 50, 0) 
		# Exercise SUT
		operacao = sistema.transferir(conta_origem, conta_destino, valor_destino)
		# Result Verification
		self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
		self.assertEqual(conta_origem.calcular_saldo(), ValorMonetario(Moeda.BRL, 10000))
		self.assertEqual(conta_destino.calcular_saldo(), ValorMonetario(Moeda.BRL, 0))
		# Fixture Teardown
