import copy

def main():
    fish = read_input()
    fish_reproduction(fish)

def fish_reproduction(input):
    fishes = input
    birth_cycle = 6
    first_cycle = 2
    days = 18

    for day in range(1,days + 1):
        new_fish = []
        current_fish = copy.deepcopy(fishes)
        for fish in range(0,len(fishes)):
            if current_fish[fish] == 0:
                current_fish[fish] = birth_cycle
                new_fish.append(birth_cycle + first_cycle)
            current_fish[fish] = current_fish[fish] - 1
        fishes = copy.deepcopy(current_fish)   
         
        if len(new_fish) > 0:
            fishes.extend(new_fish)
        print(f'After {str(day):>2} day: {fishes}')

def read_input():
    input_file = 'sample.txt'
    fish = []
    
    with open(input_file) as file:
        fish = file.readline().rstrip().split(',')
        fish = list(map(int,fish))
    return fish

if __name__ == '__main__':
    main()