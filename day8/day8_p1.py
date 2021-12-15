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

# digit 0 has 6 wires a , b , c , e , f , g 
# digit 1 has 2 wires c , f
# digit 2 has 5 wires a , c , d , e , g
# digit 3 has 5 wires a , c , d , f , g
# digit 4 has 4 wires b , c , d , f 
# digit 5 has 5 wires a , b , d , f , g
# digit 6 has 6 wires a , b , d , e , f , g
# digit 7 has 3 wires a , c , f
# digit 8 has 7 wires a , b , c , d , e , f , g
# digit 9 has 6 wires a , b , c , d , f , g