import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file, type):
        with open(file) as csv_file:
            dict_list = list(csv.DictReader(csv_file))

        if type == "simples":
            report = SimpleReport.generate(dict_list)
        elif type == "completo":
            report = CompleteReport.generate(dict_list)
        return report


# if __name__ == "__main__":
#     obj_reader = Inventory()
#     print(obj_reader.import_data(
# "/home/ruan/Projetos/sd-016-b-inventory-report/inventory_report/data/inventory.csv",
# "simples"))
#     print(obj_reader.import_data(
# "/home/ruan/Projetos/sd-016-b-inventory-report/inventory_report/data/inventory.csv",
# "completo"))
