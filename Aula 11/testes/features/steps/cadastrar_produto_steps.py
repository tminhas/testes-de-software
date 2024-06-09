from behave import given, when, then
from datetime import datetime
from mercado_leilao import MercadoLeilao

@given('o cadastro do usuario Ernani Cesar foi realizado')
def step_impl(context):
    context.mercado = MercadoLeilao()
    context.mercado.cadastra_usuario("Ernani Cesar", "Campus Universitario", "ernani.santos@posgrad.ufsc.br", "055.761.919-00")

@given('o nome do produto "{nome}"')
def step_impl(context, nome):
    context.nome_produto = nome

@given('a descricao do produto "{descricao}"')
def step_impl(context, descricao):
    context.descricao_produto = descricao

@given('o lance {lance}')
def step_impl(context, lance):
    context.lance = float(lance)

@given('o cpf do leiloador "{cpf}"')
def step_impl(context, cpf):
    context.cpf_leiloador = cpf

@given('a data limite "{data_limite}"')
def step_impl(context, data_limite):
    context.data_limite = datetime.strptime(data_limite, "%Y-%m-%d")

@when('cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(
            context.nome_produto,
            context.descricao_produto,
            context.lance,
            context.cpf_leiloador,
            context.data_limite
        )
        context.resultado = "sucesso"
    except Exception as e:
        context.resultado = str(e)

@then('o sistema cadastra com sucesso')
def step_impl(context):
    assert context.resultado == "sucesso"

@given('o produto "{nome}" com descricao "{descricao}" ja foi cadastrado')
def step_impl(context, nome, descricao):
    context.mercado.cadastra_produto(nome, descricao, 100, "055.761.919-00", datetime(2024, 12, 31))

@then('o sistema mostra a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    assert context.resultado == mensagem
