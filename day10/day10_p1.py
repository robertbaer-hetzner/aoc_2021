#!/usr/bin/env python3

import numpy as np

def get_input():
    input_data = []
    output_data = []
    with open('C:\\Git\\aoc_2021\\day10\\input.txt', 'r') as file:
        for line in file:
            input_data += line.strip().split('\n')
    for element in input_data:
        output_data.append(list(element))
    return output_data
    
#START
if __name__ == "__main__":
    symbols = get_input()
   # Zeilen print(len(symbols))
   # Spalten print(len(symbols[0]))
    score = 0
    pointes = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
    invert_last_symbol = { "(": ")", "[": "]", "{": "}", "<": ">" }

    for row in symbols:
        chunk = []
        for char in row:
            #print("Chunk",chunk)
            if len(chunk) > 0:
                last_symbol = chunk[-1]
            else:
                last_symbol = None
        
            if char in "[{(<":
                chunk.append(char)
                #print("Insert")
            elif last_symbol == "[" and char == "]":
                chunk.pop()
            elif last_symbol == "{" and char == "}":
                chunk.pop()
            elif last_symbol == "<" and char == ">":
                chunk.pop()
            elif last_symbol == "(" and char == ")":
                chunk.pop()
            else:
                score += pointes[char]
                break
    print("Syntax Error Count: ",score)