

def main():
    fish = read_input()
    print(fish)

def read_input():
    input_file = 'sample.txt'
    fish = []
    
    with open(input_file) as file:
        fish = file.readline().rstrip().split(',')
        fish = list(map(int,fish))
    return fish

if __name__ == '__main__':
    main()