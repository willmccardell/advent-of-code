from parse import *

class point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

class line:
    start_point = None
    end_point = None

    def __init__(self, p1, p2):
        self.start_point = p1
        self.end_point = p2
    
    def __str__(self):
        return f'{self.start_point} -> {self.end_point}'

def main():
    input = read_input()
    [print(l) for l in input]

def read_input():
    line_list = []
    temp_values = []
    inputFile = "sample.txt"
    
    with open(inputFile) as file:
        while (read_line := file.readline().rstrip()):
            parsed_line = parse("{},{} -> {},{}", read_line)
            #print(f'({parsed_line[0]},{parsed_line[1]}) -> ({parsed_line[2]},{parsed_line[3]})')
            start_point = point(parsed_line[0],parsed_line[1])
            end_point = point(parsed_line[2],parsed_line[3])
            new_line = line(start_point,end_point)
            line_list.append(new_line)
            
    return line_list

if __name__ == '__main__':
    main()