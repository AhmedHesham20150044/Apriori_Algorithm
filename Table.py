from itertools import combinations


class SupportTable:

    def __init__(self, pass_item=None, size=None):
        if pass_item is None and size is None:
            self.table = list()
        else:
            self.table = list()
            for subset in combinations(pass_item, size):
                self.table.append(SupportItem(set(subset), 0))

    def add_item(self, item):
        for record in self.table:
            if record.item_set == item:
                record.item_freq += 1
                return
        new_item = SupportItem(item)
        self.table.append(new_item)

    def enter_trans(self, trans):
        for subset in combinations(trans, 1):
            self.add_item(set(subset))

    def print_table(self):
        for record in self.table:
            print(record.item_set, "\t=>\t", record.item_freq)


class SupportItem:
    def __init__(self, item_set, item_freq=None):
        self.item_set = item_set
        if item_freq is None:
            self.item_freq = 1
        else:
            self.item_freq = item_freq


class ConfidesTable:
    def __init__(self, support_table):
        self.table = list()
        for record in support_table.table:
            for l in range(1, len(record.item_set)):
                for subset in combinations(record.item_set, l):
                    confides_record = ConfidesItem(record.item_set, record.item_freq, set(subset))
                    self.table.append(confides_record)

    def print_table(self):
        for record in self.table:
            print(record.dep, "\t=>\t", record.in_dep, "\t==\t", record.dep_freq/record.in_dep_freq)


class ConfidesItem:
    def __init__(self, dep, dep_freq, in_dep):
        self.dep = dep
        self.in_dep = in_dep
        self.dep_freq = dep_freq
        self.in_dep_freq = 0
