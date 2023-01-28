import copy
import re
import cProfile
import numpy as np


testcase = 0
output_info = 0
day2 = True

def main():
    fish = read_input()
    
    if day2:
        fish_reproduction_quick(fish)
    else:
        test_value = read_test_case()
        fish_chart, textual_fish = fish_reproduction_simulation(fish)
        if testcase and output_info:
            run_test(test_value, textual_fish)
        process_fish(fish_chart)
    

def process_fish(fishes):
    print(f'Number of fish: {len(fishes)}')

def run_test(test_value, fish_chart):
    if test_value != fish_chart:
        print("Does not match test case!")
    else:
        print("Test succeeds!")

#adapted from https://github.com/interannette/advent-of-code/blob/master/2021/day06/day06.go
def fish_reproduction_quick(input):
    days = 256
    fishes = input

    #populate the dictionary with keys for all possible keys
    fishcount = dict.fromkeys(range(0,9),0)
    #count how many fish there are at each stage of lifecycle
    for _, fish in enumerate(fishes):
        fishcount[fish] = fishcount[fish] + 1
    
    for day in range(0, days):
        newFishCount = dict.fromkeys(range(0,9),0)
        #for each day, shift each entry of fish down 1. if at 0, shift them into slot 8 to handle birthing
        for i in range(0,9):
            numberAtDay = fishcount[i]
            newDay, spawn = fishgrowth(i)
            newFishCount[newDay] = newFishCount[newDay] + numberAtDay
            if spawn:
                newFishCount[8] = newFishCount[8] + numberAtDay
        fishcount = newFishCount

    print(sum(fishcount.values()))

def fishgrowth(fish):
    spawn = False
    if fish == 0:
        fish = 6
        spawn = True
    else:
        fish = fish - 1
    return fish, spawn

def fish_reproduction_simulation(input):
    fishes = input
    birth_cycle = 6
    first_cycle = 2
    if testcase == 1:
        days = 18
    else:
        days = 80
    output_for_test = ""
    if output_info:
        out_str = f'Initial state: {",".join([str(i) for i in fishes])}'
        output_for_test += out_str + '\n'

    for day in range(1,days+1):
        new_fish = [birth_cycle + first_cycle for fish, age in enumerate(fishes) if age == 0]
        for i, age in enumerate(fishes):
            if age > 0:
                fishes[i] -= 1
            else:
                fishes[i] = birth_cycle
        fishes += new_fish
        if output_info:
            out_str = f'After {str(day):>2} day{"s:" if day > 1 else ": "} {",".join([str(i) for i in fishes])}'
            output_for_test += out_str + '\n'
    if output_info:
        output_for_test = output_for_test.rstrip()
        print(output_for_test)
    return fishes, output_for_test

def read_test_case():
    input_file = 'testcase.txt'
    test_value = ""
    with open(input_file) as file:
        while (read_line := file.readline()):
            test_value += read_line 
    return test_value

def read_input():
    if testcase == 1:
        input_file = "sample.txt"
    else:
        input_file = 'input.txt'
    fish = []
    
    with open(input_file) as file:
        fish = file.readline().rstrip().split(',')
        fish = list(map(int,fish))
    return fish

if __name__ == '__main__':
    main()
    #cProfile.run('main()')