import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if not file.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(file) as json_file:
            dict_list = json.load(json_file)

        return dict_list
