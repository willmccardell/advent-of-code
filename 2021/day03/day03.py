from collections import Counter
import copy

def main():
    input = read_input()
    process_power_diagnostics_report(input)
    #part 2 adapted from
    # https://github.com/interannette/advent-of-code/blob/master/2021/day03/day03.go
    process_life_support_report(input)

def process_power_diagnostics_report(input):
    most_sig = []
    least_sig = []
    width_of_report = len(input[0]) #assume equal width
    for i in range(0,width_of_report):
        slice_of_report = [val[i] for val in input]
        counter_of_slice = Counter(slice_of_report)
        most_sig.append(most_common(counter_of_slice))
        least_sig.append(least_common(counter_of_slice))

    #convert results into a single string, then convert
    #into int assuming the str is in base 2
    gamma_rate = int(''.join(map(str,most_sig)), 2)
    epsilon_rate = int(''.join(map(str,least_sig)),2)  
    
    power_output = gamma_rate * epsilon_rate

    print(f"Power output: {power_output}. Gamma: {gamma_rate} Epsilon: {epsilon_rate}")

def process_life_support_report(input):
    oxygen_rating = 0
    co2_rating = 0

    oxygen_rating = computeLifeSupportRating(input,oxygenCompare)
    co2_rating = computeLifeSupportRating(input,co2Compare)

    life_support = oxygen_rating * co2_rating

    print(f"Life Support: {life_support} Oxygen: {oxygen_rating} CO2: {co2_rating}")
    

#loop through the width
#   Have 2 deep copied lists of the input
#   If a list has more than 2 entries left, process it according
#       to the filter criteria, removing the entries that don't matter
#   Once that's done, combine the two numbers
def computeLifeSupportRating(input, comparison_func):

    max_exponent = len(input[0]) - 1 # Minus one because the first binary bit is 2^0th.
    nums = []
    for bitlist in input:
            nums.append(get_number(bitlist))

    for power in range(max_exponent,0,-1):
        current_power_of_two = pow(2,power)
        
        zeroes = []
        ones = []   

        for val in nums:
            result = val & current_power_of_two
            #print(f'num: {val} num: {num} powero2: {current_power_of_two}')
            if result == 0:
                zeroes.append(val)
            else:
                ones.append(val)
        
        compare_result = comparison_func(len(ones), len(zeroes))
        if compare_result == 1:
            nums = ones
        else:
            nums = zeroes
        
        if len(nums) <= 1:
            break

    return nums[0]


def get_number(list_of_bits):
    retval = 0
    for bit in list_of_bits:
        retval = (retval << 1) | bit
    return retval

#these next two are functions for readability of the obtuse
#most_common function
def most_common(lst):
    #print(lst.most_common())
    return lst.most_common(1)[0][0]

def least_common(lst):
    return lst.most_common()[-1][0]

def oxygenCompare(onesCount, zerosCount):
    if onesCount >= zerosCount:
        return 1
    else:
        return 0

def co2Compare(onesCount, zerosCount):
    if zerosCount <= onesCount:
        return 0
    else:
        return 1

def read_input():
    values = []
    temp_values = []
    inputFile = "input.txt"
    
    with open(inputFile) as file:
        while (line := file.readline().rstrip()):
            final_bits = [int(n) for n in list(line)]
            values.append(final_bits)

    return values

if __name__ == '__main__':
    main()