
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
    increases = 0
    for i in range(3, len(processed_data), 1):
        curr_3m_window = processed_data[i] + processed_data[i-1] + processed_data[i-2]
        prev_3m_window = processed_data[i-1] + processed_data[i-2] + processed_data[i-3]
        if curr_3m_window > prev_3m_window:
            increases = increases + 1

    return increases

if __name__ == "__main__":
    main()