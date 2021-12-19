#!/usr/bin/env python3

from itertools import chain, count
import numpy as np

def get_input():
    input_data = []
    output_data = []
    with open('C:\\Git\\aoc_2021\\day9\\input.txt', 'r') as file:
        for line in file:
            input_data += line.strip().split('\n')
    for element in input_data:
        output_data.append(list(element))
    return output_data
    
#START
if __name__ == "__main__":
"""
    all_basins = []
    covered = []
    data = get_input()
    lmax = len(data)
    dmax = len(data[0])
    risk_levels = 0

for lindex, line in enumerate(data):
    for dindex, digit in enumerate(line):
        conditions = []
        if dindex - 1 >= 0:
            conditions.append(digit < line[dindex-1])
        if dindex + 1 < dmax:
            conditions.append(digit < line[dindex+1])
        if lindex - 1 >= 0:
            conditions.append(digit < data[lindex-1][dindex])
        if lindex + 1 < lmax:
            conditions.append(digit < data[lindex+1][dindex])
        if all(conditions):
            all_basins.append({
                'lowpoint': (dindex, lindex),
                'values': []})
            risk_levels += 1 + int(digit)
print('part 1:', risk_levels)
"""
    