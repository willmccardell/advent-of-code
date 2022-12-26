from collections import Counter

def main():
    input = read_input()
    #process_power_diagnostics_report(input)
    process_life_support_report(input)

def process_life_support_report(input):

    oxygen_rating = 0
    co2_scrubber_rating = 0

    width_of_report = len(input[0]) #assume equal width
    for i in range(0,width_of_report):
        slice_of_report = [val[i] for val in input]
        counter_of_slice = Counter(slice_of_report)
        filter_reading(counter_of_slice, True)
    #take list
    #   consider first bit of number in list
    #       apply filter for the criteria
    #       only keep entries in list that match the filter
    #           if counts match, 
    #               for O2: bias to 1
    #               for CO2: bias to 0
    #       check if have more than 1 entry, if so continue

    life_support = oxygen_rating * co2_scrubber_rating
    print(f"Life Support: {life_support} Oxygen: {oxygen_rating} CO2: {co2_scrubber_rating}")



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

#these next two are functions for readability of the obtuse
#most_common function
def most_common(lst):
    #print(lst.most_common())
    return lst.most_common(1)[0][0]

def least_common(lst):
    return lst.most_common()[-1][0]

def filter_reading(lst, oxygen):
    data = lst.most_common()
    result = -1
    print(data)
    
    data.sort(key = lambda x: x[1])



def read_input():
    values = []
    temp_values = []
    inputFile = "sample.txt"
    
    with open(inputFile) as file:
        while (line := file.readline().rstrip()):
            final_bits = [int(n) for n in list(line)]
            values.append(final_bits)

    return values

if __name__ == '__main__':
    main()