import numpy as np

realdeal = False

def main():
    input = read_input()
    print(input)

def read_input():
    if realdeal == False:
        input_file = "sample.txt"
    else:
        input_file = 'input.txt'
    crabmarines = []
    
    with open(input_file) as file:
        crabmarines = file.readline().rstrip().split(',')
        crabmarines = list(map(int,crabmarines))
    
    return crabmarines

if __name__ == '__main__':
    main()