import sys
from inventory_report.importer.csv_importer import CsvImporter

from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from .inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) != 3:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        file = sys.argv[1]
        type = sys.argv[2]
        if file.endswith(".json"):
            inventory = InventoryRefactor(JsonImporter)
        elif file.endswith(".csv"):
            inventory = InventoryRefactor(CsvImporter)
        else:
            inventory = InventoryRefactor(XmlImporter)

        print(inventory.import_data(file, type), end="")


if __name__ == "__main__":
    main()
