from collections import namedtuple
Item = namedtuple("Item", ["index", "value", "weight"])

class DynamicProgramming:
    def __init__(self, capacity, items):
        self.K = capacity
        self.items = items
        self.total_value = 0
        self.decision = [0] * len(items)

    def populate_reward_matrix(self):
        self.reward_matrix = [0] * (self.K + 1)

        for i in range(len(self.items)):
            for j in range(self.K, self.items[i].weight - 1, -1):
                self.reward_matrix[j] = max(self.reward_matrix[j],
                                            self.items[i].value + self.reward_matrix[j - self.items[i].weight])

    def parse_solution(self):
        capacity = self.K
        for i in range(len(self.items) - 1, -1, -1):
            if capacity >= self.items[i].weight and \
               self.reward_matrix[capacity] == self.reward_matrix[capacity - self.items[i].weight] + self.items[i].value:
                self.decision[i] = 1
                capacity -= self.items[i].weight

        self.total_value = self.reward_matrix[self.K]

    def run(self):
        self.populate_reward_matrix()
        self.parse_solution()
