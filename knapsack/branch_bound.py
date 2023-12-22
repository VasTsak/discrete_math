from collections import namedtuple
Item = namedtuple("Item", ["index", "value", "weight"])

class Node:
    def __init__(self, level, value, weight, bound, decision):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
        self.decision = decision

class BranchAndBound:
    def __init__(self, capacity, items):
        self.K = capacity
        self.items = sorted(items, key=lambda x: x.value/x.weight, reverse=True)
        self.max_value = 0
        self.decision = []

    def bound(self, node):
        if node.weight >= self.K:
            return 0

        bound_value = node.value
        total_weight = node.weight
        level = node.level

        while level < len(self.items) and total_weight + self.items[level].weight <= self.K:
            total_weight += self.items[level].weight
            bound_value += self.items[level].value
            level += 1

        if level < len(self.items):
            bound_value += (self.K - total_weight) * (self.items[level].value / self.items[level].weight)

        return bound_value

    def run(self):
        queue = []
        queue.append(Node(-1, 0, 0, 0.0, []))

        while queue:
            node = queue.pop(0)
            if node.level == -1:
                current_decision = []
            elif node.level != len(self.items):
                current_decision = node.decision + [self.items[node.level]]

            if node.level == len(self.items) - 1:
                continue

            next_item = self.items[node.level + 1]
            next_node = Node(node.level + 1, node.value + next_item.value, node.weight + next_item.weight, 0, current_decision)
            
            if next_node.weight <= self.K and next_node.value > self.max_value:
                self.max_value = next_node.value
                self.decision = next_node.decision

            next_node.bound = self.bound(next_node)
            if next_node.bound > self.max_value:
                queue.append(next_node)

            next_node = Node(node.level + 1, node.value, node.weight, 0, node.decision)
            next_node.bound = self.bound(next_node)
            if next_node.bound > self.max_value:
                queue.append(next_node)
