from .aux_functions import oldest_fab, closest_exp, most_frequent_company


class SimpleReport():
    @classmethod
    def generate(cls, list):
        fabrication = oldest_fab(list)
        expiration = closest_exp(list)
        company = most_frequent_company(list)

        return (
          f"Data de fabricação mais antiga: {fabrication}\n"
          f"Data de validade mais próxima: {expiration}\n"
          f"Empresa com mais produtos: {company}"
        )


if __name__ == "__main__":

    lista_teste = [
     {
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
     },
     {
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2010-12-03",
       "data_de_validade": "2022-04-10",
     },
     {
       "nome_da_empresa": "Absolute",
       "data_de_fabricacao": "2002-01-02",
       "data_de_validade": "2010-12-30",
     }
    ]

    print(SimpleReport.generate(lista_teste))
