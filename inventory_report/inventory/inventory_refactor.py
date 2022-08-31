from ..importer.importer import Importer
from .inventory_iterator import InventoryIterator
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class InventoryRefactor:

    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def import_data(self, file, type):
        self.data.extend(self.importer.import_data(file))
        if type == "simples":
            return SimpleReport.generate(self.data)
        elif type == "completo":
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
