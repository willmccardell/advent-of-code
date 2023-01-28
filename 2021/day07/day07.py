import numpy as np
import cProfile

realdeal = False


def find_least_costly_position(crabmarines):
    highest_position = max(crabmarines)
    crabs = np.array(crabmarines)
    fuel_cost = crabs
    lowest_fuel = None
    converge_spot = -1
    #Meatbag's version
    # for dest in range(0,highest_position + 1):
    #     fuel_cost = abs(crabs - dest)
    #     total_fuel = sum(fuel_cost)
    #     if lowest_fuel == None:
    #         lowest_fuel = total_fuel
    #     if total_fuel < lowest_fuel:
    #         lowest_fuel = total_fuel
    #         converge_spot = dest

    #AI's for-loop version
    # fuel_cost = []
    # for dest in range(highest_position + 1):
    #     dest_cost = []
    #     for crab in crabs:
    #         dest_cost.append(abs(crab - dest))
    #     fuel_cost.append(dest_cost)

    # total_fuel = [sum(x) for x in fuel_cost]
    # lowest_fuel = min(total_fuel)
    # converge_spot = total_fuel.index(lowest_fuel)

    #AI's numpy version
    fuel_cost = np.abs(crabs[:,np.newaxis] - np.arange(highest_position+1))
    total_fuel = np.sum(fuel_cost, axis=0)
    lowest_fuel = np.min(total_fuel)
    converge_spot = np.argmin(total_fuel)

    print(f'Converging on Spot {converge_spot} costs {lowest_fuel}')

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
    #cProfile.run('main()')