#!/usr/bin/env python3

import numpy as np

class Speicher:
    def __init__(self,):
        self.board = np.zeros((10,10), dtype=int)



def get_input():
    coordinates = []
    with open('E:\\Github\\aoc_2021\\day5\\input.txt', 'r') as file:
        for line in file:
            coordinates += line.strip().split(' -> ')
    return coordinates

#START
if __name__ == "__main__":
    coordinates = get_input() 
    matrix = Speicher()
    counter = 0
    while counter < len(coordinates):
        first = coordinates[counter].split(',')
        second = coordinates[counter+1].split(',')
        x1 = int(first[0])
        y1 = int(first[1])
        x2 = int(second[0])
        y2 = int(second[1])

        if x1 == x2:
           
            if y1 < y2:
                # links ist kleiner als rechts
                while y1 < y2:
                    matrix.board[x1,y1] += 1
                    y1 += 1      
            else:
                # rechts ist kleiner als links
                while y2 > y1:
                    matrix.board[x1,y2] += 1
                    y2 -= 1  
        
        elif y1 == y2:

            if x1 < x2:
                # links ist kleiner als rechts
                while x1 < x2:
                    matrix.board[x1,y1] += 1
                    x1 += 1      
            else:
                # rechts ist kleiner als links
                while x2 > x1:
                    matrix.board[x1,y2] += 1
                    y2 -= 1  
        
        
        #print('Koord1: ',first,'\nKoord2: ',second,'\n')

        counter += 2
print(matrix.board)
