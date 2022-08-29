from inventory_report.inventory.product import Product


def test_relatorio_produto():
    'Testa o repr da classe Product'
    produto_teste = Product(
        id=1,
        nome_do_produto="Produto Teste",
        nome_da_empresa="Empresa 1",
        data_de_fabricacao="10/10/2020",
        data_de_validade="11/11/2020",
        numero_de_serie=123456,
        instrucoes_de_armazenamento="em local fresco")

    assert repr(produto_teste) == (
            f"O produto {produto_teste.nome_do_produto}"
            f" fabricado em {produto_teste.data_de_fabricacao}"
            f" por {produto_teste.nome_da_empresa} com validade"
            f" até {produto_teste.data_de_validade}"
            f" precisa ser armazenado "
            f"{produto_teste.instrucoes_de_armazenamento}."
        )
