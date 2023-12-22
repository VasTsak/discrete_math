from collections import namedtuple
Item = namedtuple("Item", ["index", "value", "weight"])

class DynamicProgramming:
    def __init__(self, capacity, items):
        self.K = capacity
        self.items = items
        self.total_value = 0
        self.total_weight = 0
        self.decision = [0] * len(items)

    def populate_reward_matrix(self):

        self.reward_matrix = [[0] * self.K for _ in range(len(self.items))]

        for i in range(len(self.items)):
            for j in range(self.K):
                if j >= self.items[i].weight:
                    if i > 0:
                        residual_weight = j - self.items[i].weight
                        value = self.items[i].value + self.reward_matrix[self.items[i].index-1][residual_weight]
                    else:
                        value = self.items[i].value
                    for s in range(i, len(self.items)):
                        self.reward_matrix[self.items[s].index][j] = value

    def parse_solution(self):

        capacity = self.K-1
        self.total_value = self.reward_matrix[len(self.items)-1][capacity]
        for item in reversed(self.items):
            
            while capacity >= 0:
                if self.reward_matrix[item.index][capacity] == self.reward_matrix[item.index-1][capacity]:
                    break
                else:
                    self.decision[item.index] = 1
                    capacity -= 1

    
    def run(self):
        self.populate_reward_matrix()
        self.parse_solution()