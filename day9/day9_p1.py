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
    return np.array(output_data, int)
    
#START
if __name__ == "__main__":
    heightmap = get_input()
    risk_level = 0
    for row in range(len(heightmap)):
        
        for column in range(len(heightmap[0])):
            
            if heightmap[row,column] == 0:
                risk_level += heightmap[row,column] + 1
                #print('Null')
            elif row == 0:
                #print('Firstline')
                if heightmap[row,column-1] > heightmap[row,column] < heightmap[row,column+1] and heightmap[row,column] < heightmap[row+1,column]:
                     risk_level += heightmap[row,column] + 1
            elif row == len(heightmap)-1:
                #print('Last Line')
                if heightmap[row,column-1] > heightmap[row,column] < heightmap[row,column+1] and heightmap[row,column] < heightmap[row-1,column]:
                     risk_level += heightmap[row,column] + 1
            elif column == 0:
                #print('First Column')
                if  heightmap[row,column] < heightmap[row,column+1] and heightmap[row-1,column] > heightmap[row,column] < heightmap[row+1,column]:
                     risk_level += heightmap[row,column] + 1
            elif column == len(heightmap[0])-1:
                #print('Last Column')
                if  heightmap[row,column] < heightmap[row,column-1] and heightmap[row-1,column] > heightmap[row,column] < heightmap[row+1,column]:
                     risk_level += heightmap[row,column] + 1
            else:
               #print('rest of the pack')
                if  heightmap[row,column+1] > heightmap[row,column] < heightmap[row,column-1] and heightmap[row-1,column] > heightmap[row,column] < heightmap[row+1,column]:
                     risk_level += heightmap[row,column] + 1

    print('Risklevel: ',risk_level)


    