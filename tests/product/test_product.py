from inventory_report.inventory.product import Product


def test_cria_produto():
    'Cria um produto pela classe Product'
    produto_teste = Product(
        id=1,
        nome_do_produto="Produto Teste",
        nome_da_empresa="Empresa 1",
        data_de_fabricacao="10/10/2020",
        data_de_validade="11/11/2020",
        numero_de_serie=123456,
        instrucoes_de_armazenamento="em local fresco")

    assert produto_teste.id == 1
    assert produto_teste.nome_do_produto == "Produto Teste"
    assert produto_teste.nome_da_empresa == "Empresa 1"
    assert produto_teste.data_de_fabricacao == "10/10/2020"
    assert produto_teste.data_de_validade == "11/11/2020"
    assert produto_teste.numero_de_serie == 123456
    assert produto_teste.instrucoes_de_armazenamento == "em local fresco"
