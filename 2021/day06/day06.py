import copy
import re
import cProfile


testcase = 1
output_info = 1


def main():
    fish = read_input()
    test_value = read_test_case()
    fish_chart, textual_fish = fish_reproduction(fish)
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

def fish_reproduction(input):
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