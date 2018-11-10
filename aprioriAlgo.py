from Table import SupportTable, ConfidesTable
from excel_file import Excel


class Apriori:

    def __init__(self, file_name, m_s, m_c):
        self.m_c = m_c
        self.m_s = m_s
        self.file_name = file_name

    def filter_support(self, data):
        index = 0
        pass_item = set()
        while index < len(data.table):
            if data.table[index].item_freq < self.m_s:
                data.table.pop(index)
            else:
                pass_item = pass_item.union(data.table[index].item_set)
                index += 1
        return pass_item

    def filter_confides(self, data):
        index = 0
        while index < len(data.table):
            if (data.table[index].dep_freq / data.table[index].in_dep_freq) < self.m_c:
                data.table.pop(index)
            else:
                index += 1
        return

    @staticmethod
    def __check_support(data):
        if len(data.table) == 0:
            print("not found supported items :( ")
            return False
        elif len(data.table[0].item_set) < 2:
            print("not found supported items :( ")
            return False
        else:
            return True

    @staticmethod
    def __check_confides(data):
        if len(data.table) == 0:
            print("not found confides items :( ")
            return False
        else:
            return True

    def calc_support(self):
        print("loading file .... \n")
        data_file = Excel(self.file_name)
        count = 1
        pass_item = set()
        previous_table = SupportTable()
        while True:
            if count == 1:
                table = data_file.create_one_item()
                print("Calculate Support\n")
            else:
                table = SupportTable(pass_item, count)
                data_file.calc_support_freq(table)
            pass_item = self.filter_support(table)
            count += 1
            if len(pass_item) == 0:
                break
            previous_table = table
        return previous_table

    def calc_confides(self, support_table):
        print("Calculate Confides")
        data_file = Excel(self.file_name)
        table = ConfidesTable(support_table)
        data_file.calc_confides_freq(table)
        self.filter_confides(table)
        self.__check_confides(table)
        table.print_table()

    def run_algorithm(self):
        data = self.calc_support()
        if self.__check_support(data):
            self.calc_confides(data)
        else:
            return
