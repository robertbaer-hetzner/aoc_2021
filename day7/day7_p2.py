#!/usr/bin/env python3
import numpy as np


def get_input():
    fish_timer = []
    with open('E:\\Git\\aoc_2021\\day7\\input.txt', 'r') as file:
        for line in file:
            fish_timer += line.split(',')
    ar = np.array(fish_timer, int) 
    return ar

#START
if __name__ == "__main__":
    numberlist = get_input().astype('int')
    store_value = 99999999999999
    new_value = 0
    counter = 0
    while counter < ( max(numberlist) - min(numberlist) ):
        numberlist_2 = []
        for element in numberlist:
            if counter >= element:
                numberlist_2.append(abs(sum(range(element,counter)+counter)))
            else:
                test = element - counter
                while test > 0:
                    
                    test -= 1

            print(sum(range(counter,element)))
        print('Allignment: ',counter,' costs ',sum(numberlist_2),' fuel. Array: ',numberlist_2)
        new_value = sum(numberlist_2)
        if new_value < store_value and new_value != 0 :
            store_value = new_value  
        counter += 1

    print('The minimal fuel costs are: ',store_value)