#!/usr/bin/env python3
import numpy as np


def get_input():
    fish_timer = []
    with open('C:\\Git\\aoc_2021\\day6\\input.txt', 'r') as file:
        for line in file:
            fish_timer += line.split(',')
    ar = np.array(fish_timer, int) 
    return ar



#START
if __name__ == "__main__":
    fishlist = get_input().astype('int')
    days = 18
    day_counter = 0

    print('Initial State: ',fishlist)
    while days > 0:
        day_counter += 1
        for element in fishlist:
            if element == 0:
                element = 6
                fishlist.append(int(8))
            elif element > 0:
                element -= 1
           
        days -= 1
        print('After ',day_counter,' day:',fishlist)
        
