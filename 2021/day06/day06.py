import copy

testcase = 0

def main():
    fish = read_input()
    test_value = read_test_case()
    fish_chart, textual_fish = fish_reproduction(fish)
    if testcase == 1:
        run_test(test_value, textual_fish)
    process_fish(fish_chart)
    

def process_fish(fishes):
    print(f'Number of fish: {len(fishes)}')

def run_test(test_value, fish_chart):
    if test_value != fish_chart:
        print("Does not match test case!")
    else:
        print("Test succeeds!")

def fish_reproduction(input):
    fishes = input
    birth_cycle = 6
    first_cycle = 2
    if testcase == 1:
        days = 18
    else:
        days = 80
    output_for_test = ""
    out_str = f'Initial state: {",".join([str(i) for i in fishes])}'
    #print(out_str)
    output_for_test += out_str
    for day in range(1,days + 1):
        new_fish = []
        current_fish = copy.deepcopy(fishes)
        for fish in range(0,len(fishes)):
            if current_fish[fish] == 0:
                current_fish[fish] = birth_cycle
                new_fish.append(birth_cycle + first_cycle)
            else:
                current_fish[fish] = current_fish[fish] - 1
        fishes = copy.deepcopy(current_fish)   
         
        if len(new_fish) > 0:
            fishes.extend(new_fish)
        out_str = f'After {str(day):>2} day{"s:" if day > 1 else ": "} {",".join([str(i) for i in fishes])}'
        output_for_test += out_str
        #print(out_str)
    return fishes, output_for_test

def read_test_case():
    input_file = 'testcase.txt'
    test_value = ""
    with open(input_file) as file:
        while (read_line := file.readline().rstrip()):
            test_value += read_line 
    return test_value

def read_input():
    if testcase == 1:
        input_file = "sample.txt"
    else:
        input_file = 'input.txt'
    fish = []
    
    with open(input_file) as file:
        fish = file.readline().rstrip().split(',')
        fish = list(map(int,fish))
    return fish

if __name__ == '__main__':
    main()