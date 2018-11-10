import xlrd
from Table import SupportTable


class Excel:

    def __init__(self, file_name):
        wb = xlrd.open_workbook(file_name)
        self.__sheet = wb.sheet_by_index(0)

    def create_one_item(self):
        table = SupportTable()
        for row in range(1, self.__sheet.nrows):
            trans = set()
            for col in range(3, 6):
                trans.add(self.__sheet.cell_value(row, col))
            table.enter_trans(trans)
        return table

    def calc_support_freq(self, data):
        for row in range(1, self.__sheet.nrows):
            trans = set()
            for col in range(3, 6):
                trans.add(self.__sheet.cell_value(row, col))
            for record in data.table:
                if record.item_set <= trans:
                    record.item_freq += 1;
        return data

    def calc_confides_freq(self, data):
        for row in range(1, self.__sheet.nrows):
            trans = set()
            for col in range(3, 6):
                trans.add(self.__sheet.cell_value(row, col))
            for record in data.table:
                if record.in_dep <= trans:
                    record.in_dep_freq += 1;
        return data