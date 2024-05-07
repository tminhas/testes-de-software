import unittest 
from Teste_Dinheiro import TestDinheiro
from Teste_ValorMonetario import TestValorMonetario
from Teste_Transacao import TestTransacao
from Teste_Agencia import TestAgencia
from Teste_Conta import TestConta
from Teste_Banco import TestBanco
from Teste_SistemaBancario import TestSistemaBancario


if __name__ == "__main__":
	tests = unittest.TestSuite()
	loader = unittest.TestLoader()

	tests.addTest(loader.loadTestsFromTestCase(TestDinheiro))
	tests.addTest(loader.loadTestsFromTestCase(TestValorMonetario))
	tests.addTest(loader.loadTestsFromTestCase(TestTransacao))
	tests.addTest(loader.loadTestsFromTestCase(TestAgencia))
	tests.addTest(loader.loadTestsFromTestCase(TestConta))
	tests.addTest(loader.loadTestsFromTestCase(TestBanco))
	tests.addTest(loader.loadTestsFromTestCase(TestSistemaBancario))
	
	runner = unittest.TextTestRunner()
	runner.run(tests)
