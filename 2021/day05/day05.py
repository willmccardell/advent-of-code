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

    def max_x_cardinality(self):
        return max(self.start_point.x, self.end_point.x)
    
    def max_y_cardinality(self):
        return max(self.start_point.y, self.end_point.y)

class ventmap:
    lines = []
    x_bounds = None
    y_bounds = None
    vmap = None

    def __init__(self,lines):
        self.lines = lines
        
        #need to iterate through lines to find the max points
        self.x_bounds = max([l.max_x_cardinality() for l in self.lines])
        self.y_bounds = max([l.max_y_cardinality() for l in self.lines])
        #prepopulate the vmap
        self.vmap = [[0 for x in range(self.x_bounds)] for x in range(self.y_bounds)]

    def __str__(self):
        #for row in self.vmap:
          
        return ''

def main():
    input = read_input()
    vents = ventmap(input)
    [print(l) for l in vents.lines]
    print(f'Max Size: {vents.x_bounds}, {vents.y_bounds}')
    print(vents)

def read_input():
    line_list = []
    temp_values = []
    inputFile = "sample.txt"
    
    with open(inputFile) as file:
        while (read_line := file.readline().rstrip()):
            parsed_line = parse("{:d},{:d} -> {:d},{:d}", read_line)
            #print(f'({parsed_line[0]},{parsed_line[1]}) -> ({parsed_line[2]},{parsed_line[3]})')
            start_point = point(parsed_line[0],parsed_line[1])
            end_point = point(parsed_line[2],parsed_line[3])
            new_line = line(start_point,end_point)
            line_list.append(new_line)
            
    return line_list

if __name__ == '__main__':
    main()