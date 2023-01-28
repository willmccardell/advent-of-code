import numpy as np
import cProfile

realdeal = False


def find_least_costly_position(crabmarines):
    highest_position = max(crabmarines)
    crabs = np.array(crabmarines)

    #ChatGPT generated
    #Creates an array that contains the position and (original) cost to get there
    fuel_cost = np.abs(crabs[:,np.newaxis] - np.arange(highest_position+1))
    #uses triangle numbers to get the full cost given the new constraints
    fuel_cost = fuel_cost*(fuel_cost+1)//2
    #sums all the fuel costs and puts it into an array
    total_fuel = np.sum(fuel_cost, axis=0)

    lowest_fuel = np.min(total_fuel)
    
    #finds the spot that the crabs are converging on
    converge_spot = np.argmin(total_fuel)

    print(f'Converging on Spot {converge_spot} costs {lowest_fuel}')

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
    #cProfile.run('main()')