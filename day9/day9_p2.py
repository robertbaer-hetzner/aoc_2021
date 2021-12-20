#!/usr/bin/env python3
from heapq import nlargest
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
    return np.array(output_data, int)
    
#START

if __name__ == "__main__":
    heightmap = get_input()
    sizes = []
    membership = set()
    for row in range(len(heightmap)):
        for column in range(len(heightmap[0])):
            candidates = [(row, column)]
            basin_size = 0
            while len(candidates) > 0:
                candidate = candidates.pop()
                ci, cj = candidate
                if ci < 0 or ci >= len(heightmap):
                    continue
                if cj < 0 or cj >= len(heightmap[0]):
                    continue
                if heightmap[ci][cj] >= 9:
                    continue
                if candidate in membership:
                    continue

                basin_size += 1
                membership.add(candidate)
                candidates.append((ci + 1, cj))
                candidates.append((ci - 1, cj))
                candidates.append((ci, cj + 1))
                candidates.append((ci, cj - 1))

            if basin_size > 0:
                sizes.append(basin_size)

    largest = list(nlargest(3, sizes))
    basin =  largest[0] * largest[1] * largest[2]
    print("3 largest Basin combined: ", basin)


    