#!/usr/bin/env python3

def get_input():
    segments = []
    with open('E:\\Git\\aoc_2021\\day8\\input.txt', 'r') as file:
        for line in file:
            segments += line.strip().split(' | ')[1].split(' ')
    return segments

def selector(x):
    if len(x) >= 2 or len(x) <= 4 or len(x) == 7:
        return True
    return False
    
#START
if __name__ == "__main__":
    segments = get_input()
    print(segments)
    segments = list(filter(selector(), segments))
    print('result: ', len(segments))
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