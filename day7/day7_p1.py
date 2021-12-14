#!/usr/bin/env python3
import numpy as np


def get_input():
    fish_timer = []
    with open('C:\\Git\\aoc_2021\\day7\\input.txt', 'r') as file:
        for line in file:
            fish_timer += line.split(',')
    ar = np.array(fish_timer, int) 
    return ar



#START
if __name__ == "__main__":
    numberlist = get_input().astype('int')

    print(min(numberlist))
    print(max(numberlist))

    