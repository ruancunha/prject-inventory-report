from .simple_report import SimpleReport
from .aux_functions import company_products


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        result = company_products(list)

        return (
          f"{super().generate(list)}\n"
          f"{result}")


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
     },
     {
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
     },
     {
       "nome_da_empresa": "Test",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
     },
     {
       "nome_da_empresa": "Test",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
     },
    ]

    print(CompleteReport.generate(lista_teste))
