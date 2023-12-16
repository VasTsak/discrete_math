from collections import namedtuple
Item = namedtuple("Item", ["index", "value", "weight"])
ItemGreedy = namedtuple("ItemGreedy", ["index", "value", "weight", "value_weight"])

class Greedy:
    def __init__(self, capacity, items):
        self.K = capacity
        self.items = items
        self.total_value = 0
        self.total_weight = 0
        self.decision = [0] * len(items)

    def sort_value_ratio(self):

        self.items = [ItemGreedy(i, v, w, v/w) for i, v, w in self.items]
        self.items = sorted(self.items, key=lambda x: x.value_weight)
    
    def run(self):

        for item in self.items:
            if item.weight <= self.K:
                self.decision[item.index] = 1
                self.K -= item.weight
                self.total_value += item.value
    