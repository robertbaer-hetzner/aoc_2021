#!/usr/bin/env python3

from itertools import chain, count
import numpy as np

def get_input():
    input_data = []
    output_data = []
    with open('E:\\Git\\aoc_2021\\day9\\input.txt', 'r') as file:
        for line in file:
            input_data += line.strip().split('\n')
    for element in input_data:
        output_data.append(list(element))
    return output_data
    
#START
if __name__ == "__main__":
    segments = np.array(get_input())
    row_counter = 0
    low_points = 0
    while row_counter < len(segments):
        line_counter = 0
        while line_counter < len(segments[row_counter]):
            if segments[row_counter,line_counter] == 0:
                low_points += 1
            elif line_counter == 0 or line_counter == len(segments[row_counter]):
                #here check edge points
                if segments[row_counter,line_counter] < segments[row_counter,line_counter]
            elif line_counter > 0 and line_counter < len(segments[row_counter]):
                #here check inlines
                print()
            line_counter += 1
        row_counter += 1

    