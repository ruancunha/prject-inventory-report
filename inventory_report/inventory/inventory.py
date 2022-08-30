import csv
import json
from xml.etree import ElementTree as ET
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:

    @classmethod
    def import_data(cls, file, type):
        if file.endswith(".csv"):
            return Inventory.data_from_csv(file, type)
        elif file.endswith(".json"):
            return Inventory.data_from_json(file, type)
        elif file.endswith(".xml"):
            return Inventory.data_from_xml(file, type)

    @classmethod
    def data_from_csv(cls, file, type):
        with open(file) as csv_file:
            dict_list = list(csv.DictReader(csv_file))

        return Inventory.define_type(dict_list, type)

    @classmethod
    def data_from_json(cls, file, type):
        with open(file) as json_file:
            dict_list = json.load(json_file)

        return Inventory.define_type(dict_list, type)

    @classmethod
    def data_from_xml(cls, file, type):
        tree = ET.parse(file)
        root = list(tree.getroot())
        dict_list = []
        info_dict = {}

        for elem in root:
            for info in elem:
                info_dict[info.tag] = info.text

            dict_list.append(info_dict)
            info_dict = {}

        return Inventory.define_type(dict_list, type)

    @classmethod
    def define_type(cls, file, type):
        if type == "simples":
            report = SimpleReport.generate(file)
        elif type == "completo":
            report = CompleteReport.generate(file)
        return report
