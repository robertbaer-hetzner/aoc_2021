#!/usr/bin/env python3

import numpy as np
import math

class Speicher:
    def __init__(self,):
        self.board = np.zeros((1000,1000), dtype=int)



def get_input():
    coordinates = []
    with open('C:\\Git\\aoc_2021\\day5\\input.txt', 'r') as file:
        for line in file:
            coordinates += line.strip().split(' -> ')
    return coordinates

def zaehler(array):
    zaehler1 = 0
    zaehler2 = 0
    overlaps = 0
    while zaehler2 < 1000:
        while zaehler1 < 1000:
            if array[zaehler2,zaehler1] > 1:
                overlaps += 1
            zaehler1 += 1
        zaehler1 = 0
        zaehler2 += 1
    
    return overlaps

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
           # print('x1 = x2\nKoord1: ',first,'\nKoord2: ',second,'\n')
            if y1 < y2:
                # links ist kleiner als rechts
                while y1 < y2 + 1:
                    matrix.board[y1,x1] += 1
                    y1 += 1      
            else:
                # rechts ist kleiner als links
                while y1 > y2 - 1:
                    matrix.board[y1,x1] += 1
                    y1 -= 1  
        
        elif y1 == y2:
          #  print('y1 = y2\nKoord1: ',first,'\nKoord2: ',second,'\n')
            if x1 < x2:
                # links ist kleiner als rechts
                while x1 < x2 + 1:
                 #   print(x1,y1)
                    matrix.board[y1,x1] += 1
                    x1 += 1      
            else:
                # rechts ist kleiner als links
                while x1 > x2 - 1:
                    matrix.board[y1,x1] += 1
                    x1 -= 1 
        else: 
           # differenz = int(math.dist([x1],[x2]))
            # x1 > x2 and y1 > y2
            if x1 > x2 and y1 > y2:
                differenz = int(math.dist([x1],[x2]))
                for zz in range(0, differenz):
                    matrix.board[y1,x1] += 1
                  #  print('Y ',y1,'X ',x1,'Diff ',differenz)
                   # print(matrix.board)
                    #differenz -= 1
                    y1 -= 1
                    x1 -= 1
                matrix.board[y1,x1] += 1
                
            # x1 < x2 and y1 < y2
            if x1 < x2 and y1 < y2:
                differenz = int(math.dist([x1],[x2]))
                while differenz >= 0:
                  # print('Y ',y1,'X ',x1,'Diff ',differenz)
                   matrix.board[y1,x1] += 1
                   differenz -= 1
                   y1 += 1
                   x1 += 1
            # x1 < x2 and y1 > y2
            if x1 < x2 and y1 > y2:
                differenz = int(math.dist([x1],[x2]))
                while differenz > 0:
                   #print('Y ',y1,'X ',x1,'Diff ',differenz)
                   matrix.board[y1,x1] += 1
                   differenz -= 1
                   y1 -= 1
                   x1 += 1
                matrix.board[y1,x1] += 1
            # x1 > x2 and y1 < y2
            if x1 > x2 and y1 < y2:
                differenz = int(math.dist([x1],[x2]))
                while differenz >= 0:
                  # print('Y ',y1,'X ',x1,'Diff ',differenz)
                   matrix.board[y1,x1] += 1
                   differenz -= 1
                   y1 += 1
                   x1 -= 1

        counter += 2
print(matrix.board)
print('Number of overlaping Points: ',zaehler(matrix.board))

