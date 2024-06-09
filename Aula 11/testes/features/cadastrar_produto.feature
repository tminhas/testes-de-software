Feature: Cadastrar Produto

  Background:
    Given o cadastro do usuario Ernani Cesar foi realizado

  Scenario: Cadastrar Produto com Sucesso
    Given o nome do produto "sofa"
    And a descricao do produto "amarelo"
    And o lance 100
    And o cpf do leiloador "055.761.919-00"
    And a data limite "2024-12-31"
    When cadastrar o produto
    Then o sistema cadastra com sucesso

  Scenario: Cadastro de Produto com Problema
    Given o produto "sofa" com descricao "amarelo" ja foi cadastrado
    And o nome do produto "sofa"
    And a descricao do produto "amarelo"
    And o lance 100
    And o cpf do leiloador "055.761.919-00"
    And a data limite "2024-12-31"
    When cadastrar o produto
    Then o sistema mostra a mensagem "O produto ja existe ou o leiloador nao esta cadastrado."
