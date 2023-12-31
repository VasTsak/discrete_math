#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from greedy_search import Greedy
from dynamic_programming import DynamicProgramming
from branch_bound import BranchAndBound

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    # greedy_search = Greedy(capacity=capacity, items=items)
    dp = DynamicProgramming(capacity=capacity, items=items)
    ### Baseline ###
    # for item in items:
       
        # if weight + item.weight <= capacity:
        #     taken[item.index] = 1
        #     value += item.value
        #     weight += item.weight

    ###Greedy Search ###

    # greedy_search.run()
    # value = greedy_search.total_value
    # taken = greedy_search.decision
    
    ###Dynamic Programming ###

    # dp.run()
    # value = dp.total_value
    # taken = dp.decision
    
    bb = BranchAndBound(capacity=capacity, items=items)
    bb.run()
    value = bb.max_value
    taken = bb.decision

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

