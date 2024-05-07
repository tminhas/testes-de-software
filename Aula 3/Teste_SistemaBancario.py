import unittest 
from dinheiro import Moeda, Dinheiro, ValorMonetario
from sistema_bancario import SistemaBancario
from operacao import EstadosDeOperacao
from hamcrest import assert_that, equal_to, is_not, none

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
        # Implicit Fixture Setup
        sistema = SistemaBancario()
        # Exercise SUT
        banco = sistema.criar_banco("Banco Teste", Moeda.BRL)
        # Result Verification
        assert_that(banco, is_not(none()))
        assert_that(banco.nome, equal_to("Banco Teste"))
        assert_that(banco.moeda, equal_to(Moeda.BRL))

    def test_obter_banco(self):
        # Delegated Fixture Setup
        sistema, banco = TestHelper.criar_sistema_bancario_com_banco()
        # Exercise SUT
        banco_obtido = sistema.obter_banco("Banco Teste")
        # Result Verification
        assert_that(banco_obtido, is_not(none()))
        assert_that(banco_obtido, equal_to(banco))
        # Fixture Teardown

    def test_depositar(self):
        # Delegated + Inline Fixture Setup
        sistema, banco = TestHelper.criar_sistema_bancario_com_banco()
        conta = TestHelper.criar_conta_em_banco(banco, "Thomas")
        quantia_deposito = Dinheiro(Moeda.BRL, 100, 0)
        saldo_atual = conta.calcular_saldo()
        # Exercise SUT
        operacao = sistema.depositar(conta, quantia_deposito)
        # Result Verification
        assert_that(operacao.obter_estado(), equal_to(EstadosDeOperacao.SUCESSO))
        assert_that(saldo_atual, equal_to(ValorMonetario(Moeda.BRL, 10000)))
        # Fixture Teardown
