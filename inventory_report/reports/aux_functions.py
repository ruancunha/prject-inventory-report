import datetime as dt


def oldest_fab(list):
    oldest_fabrication = dt.date.today()
    for product in list:
        data_fabri = dt.date(*map(
          int,
          product["data_de_fabricacao"].split("-")))
        if data_fabri < oldest_fabrication:
            oldest_fabrication = data_fabri

    return oldest_fabrication


def closest_exp(list):
    closest_expiration = dt.date(9999, 1, 1)
    for product in list:
        data_vali = dt.date(*map(
          int,
          product["data_de_validade"].split("-")))
        if data_vali >= dt.date.today():
            if data_vali < closest_expiration:
                closest_expiration = data_vali
    return closest_expiration


def most_frequent_company(list):
    filtered = [product["nome_da_empresa"] for product in list]
    return max(filtered, key=lambda x: filtered.count(x))


def company_products(list):
    companies = dict()
    for product in list:
        if product["nome_da_empresa"] in companies:
            companies[product["nome_da_empresa"]] += 1
        else:
            companies[product["nome_da_empresa"]] = 1

    return format_report(companies)


def format_report(dict):
    result = "Produtos estocados por empresa:"
    for company in dict.keys():
        result += f"\n- {company}: {dict[company]}"

    return result
