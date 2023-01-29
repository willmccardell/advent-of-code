realdeal = False

def main():
    unique_signal, fdov = read_input()
    print(unique_signal)

    print(fdov)
cd 
def read_input():
    if realdeal == False:
        input_file = "sample.txt"
    else:
        input_file = 'input.txt'
    data = []
    
    with open(input_file) as file:
        data = file.readline().rstrip().split('|')
        unique_signal_pattern = data[0].strip().split(' ')
        four_digit_output_value = data[1].strip().split(' ')
    
    return unique_signal_pattern, four_digit_output_value

if __name__ == '__main__':
    main()
    #cProfile.run('main()')