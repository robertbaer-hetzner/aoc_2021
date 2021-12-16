#!/usr/bin/env python3

def get_input():
    input_data = []
    output_data = []
    with open('/Users/robertbaer/scripte/aoc_2021/day9/input.txt', 'r') as file:
        for line in file:
            input_data += line.strip().split('\n')
    for element in input_data:
        output_data
    return output_data

def selector(x):
    if len(x) >= 2 or len(x) <= 4 or len(x) == 7:
        return True
    return False
    
#START
if __name__ == "__main__":
    segments = get_input()
    print(segments)