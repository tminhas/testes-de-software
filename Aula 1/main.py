import unittest
import datetime

class TesteDatetime(unittest.TestCase):

	def test_contem_datetime(self):
	# Fixture Setup
		current_date = datetime.datetime.now()
	# Exercise SUT
		result = isinstance(current_date, datetime.datetime)
	# Result Verification
		self.assertTrue(result)
	# Fixture Teardown

	def test_adicao(self):
	# Fixture Setup
		date = datetime.date(2024, 3, 10)
		variacao =datetime.timedelta(days=5)
		result = datetime.date(2024, 3, 15)
	# Exercise SUT
		add_day = date + variacao
	# Result Verification
		self.assertEqual(result, add_day)
	# Fixture Teardown

	def test_subtracao(self):
	# Fixture Setup
		date = datetime.date(2024,3, 10)
		variacao = datetime.timedelta(days=5)
		result = datetime.date(2024, 3, 5)
	# Exercise SUT
		subtract_day = date - variacao
	# Result Verification
		self.assertEqual(result, subtract_day)
	# Fixture Teardown


	def test_ano_bissexto_correto(self):
	# Fixture Setup
		bissexto_correto = datetime.date(2024, 3, 10)
	# Exercise SUT
		year = bissexto_correto.year
	# Result Verification
		self.assertTrue(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
	# Fixture Teardown

	def test_ano_bissexto_incorreto(self):
	# Fixture Setup
		bissexto_incorreto = datetime.date(5, 3, 10)
	# Exercise SUT
		year = bissexto_incorreto.year
	# Result Verification
		self.assertFalse(year % 4 == 0 and (year % 100 != 0  or year % 400 == 0))
	# Fixture Teardown

	def test_cria_mes_negativo(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(2024, -3, 10)
	# Result Verification
	# Fixture Teardown

	def test_cria_dia_negativo(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(2024, 3, -10)
	# Result Verification
	# Fixture Teardown

	def test_cria_ano_negativo(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(-2024, 3, 10)
	# Result Verification
	# Fixture Teardown

	def test_dia_fora_do_limite_superior(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(2024, 3, 35)
	# Result Verification
	# Fixture Teardown

	def test_mes_fora_do_limite_superior(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(2024, 15, 10)
	# Result Verification
	# Fixture Teardown

	def test_dia_zero(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(2024, 3, 0)
	# Result Verification
	# Fixture Teardown

	def test_mes_zero(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(2024, 0, 10)
	# Result Verification
	# Fixture Teardown

	def test_ano_zero(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(0, 3, 10)
	# Result Verification
	# Fixture Teardown

	def test_dia_da_semana_correto(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 3, 20).weekday()
	# Result Verification
		self.assertEqual(2, date)
	# Fixture Teardown

	def test_data_nula(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(0, 0, 0)
	# Result Verification
	# Fixture Teardown

	def test_data_negativa(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(-2024, -3, -10)
	# Result Verification
	# Fixture Teardown

	def test_primeiro_de_janeiro(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 1, 1)
	# Result Verification
		self.assertEqual(2024, date.year)
		self.assertEqual(1, date.month)
		self.assertEqual(1, date.day)
	# Fixture Teardown

	def test_data_futura(self):
	# Fixture Setup
		current_date = datetime.date(2024, 3, 20)
	# Exercise SUT
		future_date = datetime.date(2025, 1, 1)
	# Result Verification
		self.assertGreater(future_date, current_date)
	# Fixture Teardown

	def test_data_passada(self):
	# Fixture Setup
		current_date = datetime.date(2024, 3, 20)
	# Exercise SUT
		past_date = datetime.date(2023, 1, 1)
	# Result Verification
		self.assertLess(past_date, current_date)
	# Fixture Teardown

	def test_trinta_e_um_de_marco(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 3, 31)
	# Result Verification
		self.assertEqual(2024, date.year)
		self.assertEqual(3, date.month)
		self.assertEqual(31, date.day)
	# Fixture Teardown

	def test_vinte_e_nove_de_fevereiro_valido(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 2, 29)
	# Result Verification
		self.assertEqual(2024, date.year)
		self.assertEqual(2, date.month)
		self.assertEqual(29, date.day)
	# Fixture Teardown

	def test_vinte_e_nove_de_fevereiro_invalido(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(2025, 2, 29)
	# Result Verification
	# Fixture Teardown

	def test_cinco_de_maio(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 5, 5)
	# Result Verification
		self.assertEqual(2024, date.year)
		self.assertEqual(5, date.month)
		self.assertEqual(5, date.day)
	# Fixture Teardown

	def test_trinta_e_um_de_dezembro(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 12, 31)
	# Result Verification
		self.assertEqual(2024, date.year)
		self.assertEqual(12, date.month)
		self.assertEqual(31, date.day)
	# Fixture Teardown

	def test__dia_tiradentes(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 4, 21)
	# Result Verification
		self.assertEqual(2024, date.year)
		self.assertEqual(4, date.month)
		self.assertEqual(21, date.day)
	# Fixture Teardown

	def test_dia_da_independencia(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 9, 7)
	# Result Verification
		self.assertEqual(2024, date.year)
		self.assertEqual(9, date.month)
		self.assertEqual(7, date.day)
	# Fixture Teardown

	def test_dia_do_professor(self):
	# Fixture Setup
	# Exercise SUT
		date = datetime.date(2024, 10, 15)
	# Result Verification
		self.assertEqual(2024, date.year)
		self.assertEqual(10, date.month)
		self.assertEqual(15, date.day)
	# Fixture Teardown

	def test_trinta_e_um_de_novembro(self):
	# Fixture Setup
	# Exercise SUT
		with self.assertRaises(ValueError):
			date = datetime.date(2025, 11, 31)
	# Result Verification
	# Fixture Teardown

if __name__ == "__main__":
	unittest.main()
