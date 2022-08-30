import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".csv"):
            with open(file) as csv_file:
                dict_list = list(csv.DictReader(csv_file))
            return dict_list
        else:
            raise ValueError("Arquivo inválido")
