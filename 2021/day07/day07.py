import numpy as np

realdeal = True


def find_least_costly_position(crabmarines):
    highest_position = max(crabmarines)
    crabs = np.array(crabmarines)
    fuel_cost = crabs
    lowest_fuel = None
    converge_spot = -1
    for dest in range(0,highest_position + 1):
        fuel_cost = abs(crabs - dest)
        total_fuel = sum(fuel_cost)
        if lowest_fuel == None:
            lowest_fuel = total_fuel
        if total_fuel < lowest_fuel:
            lowest_fuel = total_fuel
            converge_spot = dest
    print(f'Convering on Spot {converge_spot} costs {lowest_fuel}')

def calc_fuel(pos,dest):
    return pos - dest

def main():
    input = read_input()
    find_least_costly_position(input)

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