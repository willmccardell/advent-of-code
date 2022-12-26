from collections import Counter

def main():
    input = read_input()
    process_diagnostic_report(input)
    

def process_diagnostic_report(input):
    most_sig = []
    least_sig = []
    #process_diagnostic_report(input)
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

    print(gamma_rate)
    print(epsilon_rate)

    power_output = gamma_rate * epsilon_rate

    print(power_output)

#these next two are functions for readability of the obtuse
#most_common function
def most_common(lst):
    return lst.most_common(1)[0][0]

def least_common(lst):
    return lst.most_common()[-1][0]

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