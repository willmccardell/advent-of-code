from collections import Counter

def main():
    input = read_input()
    #process_diagnostic_report(input)
    for i in range(0,5):
        print(most_common([val[i] for val in input]))

def process_diagnostic_report(input):
    for row in input:
        print(row[1])

def most_common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

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