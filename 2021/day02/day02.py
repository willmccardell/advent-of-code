
def main():
    commands = read_input()
    process_commands(commands)
    
    
def process_commands(commands):
    horiz_pos = 0
    depth = 0

    for (cmd, mag) in commands:
        match cmd:
            case 'forward':
                horiz_pos = horiz_pos + mag
            case 'down': 
                depth = depth + mag
            case 'up':
                depth = depth - mag
    total = horiz_pos * depth
    print(total)

def read_input():
    inputFile = "input.txt"
    
    commands = []
    with open(inputFile) as file:
        for line in file:
            command, magnitude = line.split()
            commands.append(tuple((command, int(magnitude))))

    return commands

if __name__ == "__main__":
    main()