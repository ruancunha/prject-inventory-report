from xml.etree import ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if not file.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(file)
        root = list(tree.getroot())
        dict_list = []
        info_dict = {}

        for elem in root:
            for info in elem:
                info_dict[info.tag] = info.text

            dict_list.append(info_dict)
            info_dict = {}

        return dict_list
