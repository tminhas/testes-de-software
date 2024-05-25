import unittest

from empresa import Empresa
from funcionario import Funcionario
from projeto import Projeto
from ocorrencia import Ocorrencia

class TestsTDD2(unittest.TestCase):

    def setUp(self):
        self.reivax = Empresa('Reivax')

    def test_1_ocorrencia_inicializacao(self):
        jose = Funcionario("José", 30, "123.456.789-00")
        ocorrencia = Ocorrencia("Tarefa 1", "alta", jose)
        
        self.assertEqual(ocorrencia.nome, "Tarefa 1")
        self.assertEqual(ocorrencia.prioridade, "alta")
        self.assertEqual(ocorrencia.funcionario, jose)
        self.assertEqual(ocorrencia.status, 1)  
        self.assertGreater(ocorrencia.id, 0)  

    def test_2_inclusao_ocorrencia_projeto(self):
            projeto = self.reivax.cria_projeto("Matanzas")
            jose = self.reivax.contrata_funcionario("José", 30, "123.456.789-00")
            
            projeto.cria_ocorrencia("Tarefa 1", "alta", jose)
            
            self.assertEqual(len(projeto.ocorrencias), 1)
            self.assertEqual(projeto.ocorrencias[0].nome, "Tarefa 1")

    def test_3_limite_de_ocorrencias(self):
            projeto = self.reivax.cria_projeto("Matanzas")
            jose = self.reivax.contrata_funcionario("José", 30, "123.456.789-00")
            
            for i in range(10):
                projeto.cria_ocorrencia(f"Tarefa {i+1}", "alta", jose)
            
            with self.assertRaises(Exception):
                projeto.cria_ocorrencia("Tarefa 11", "alta", jose)
            
            self.assertEqual(jose.ocorrencias, 10)

    def test_4_modificacao_prioridade_ocorrencia(self):
        projeto = self.reivax.cria_projeto("Matanzas")
        jose = self.reivax.contrata_funcionario("José", 30, "123.456.789-00")
        
        ocorrencia = projeto.cria_ocorrencia("Tarefa 1", "alta", jose)
        ocorrencia.prioridade = "baixa"
        
        self.assertEqual(ocorrencia.prioridade, "baixa")

    def test_5_conclusao_ocorrencia(self):
        projeto = self.reivax.cria_projeto("Matanzas")
        jose = self.reivax.contrata_funcionario("José", 30, "123.456.789-00")
        
        ocorrencia = projeto.cria_ocorrencia("Tarefa 1", "alta", jose)
        ocorrencia.fecha_ocorrencia()
        
        self.assertEqual(ocorrencia.status, 0)
        self.assertEqual(jose.ocorrencias, 0)

    def test_6_ocorrencia_id_unico(self):
        jose = Funcionario("José", 30, "123.456.789-00")
        ocorrencia1 = Ocorrencia("Tarefa 1", "alta", jose)
        ocorrencia2 = Ocorrencia("Tarefa 2", "baixa", jose)
        
        self.assertNotEqual(ocorrencia1.id, ocorrencia2.id)

if __name__ == '__main__':
    unittest.main()
