
def main():
    measurements = read_depth_measurements()
    number_increases = process_measurements(measurements)
    print(number_increases)

def read_depth_measurements():
    inputFile = "input.txt"
    
    print("Reading measurements")
    with open(inputFile) as file:
        lines = file.readlines()
    numbers = [int(n.strip()) for n in lines]
    return numbers

def process_measurements(measurements):
    processed_data = measurements

    #need to iterate through the list and get a count of number 
    #of entries that are larger than their previous one, keeping
    #in mind the off-by-one errors
    ctr = -1
    increases = 0
    for i in processed_data:
        ctr = ctr + 1
        if (ctr == 0):
            continue
        if(i > processed_data[ctr - 1]):
            increases = increases + 1

    return increases

if __name__ == "__main__":
    main()