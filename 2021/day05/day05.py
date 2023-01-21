from parse import *
import time
from itertools import chain

class point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


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

    #https://github.com/ebouteillon/advent-of-code-2021/blob/main/day-05/part2.py
    def find_path(self):
        points = []
        p1 = self.start_point
        p2 = self.end_point

        #assuming all data is either a straight line or a 45 degree angle
        if p1.x == p2.x or p1.y == p2.y:
            #reorder them to always go in the same direction
            x1, y1, x2, y2 = min(p1.x,p2.x), min(p1.y,p2.y), max(p1.x,p2.x), max(p1.y,p2.y)
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    points.append(point(x,y))
        else:
            # orient the direction of the line and get all
            # entries along the two points    
            x = range(p1.x, p2.x +1) if p1.x <= p2.x else range(p1.x, p2.x -1, -1)
            y = range(p1.y, p2.y +1) if p1.y <= p2.y else range(p1.y, p2.y -1, -1)
            for i,j in zip(x,y):
                points.append(point(i,j))
        return points

class ventmap:
    lines = []
    x_bounds = None
    y_bounds = None
    vent_map = None

    def __init__(self,lines):
        self.lines = lines
        
        #need to iterate through lines to find the max points
        self.x_bounds = max([l.max_x_cardinality() for l in self.lines])
        self.y_bounds = max([l.max_y_cardinality() for l in self.lines])
        #prepopulate the vmap
        self.vent_map = [[0 for x in range(self.x_bounds + 1)] for x in range(self.y_bounds + 1)]

        for line in self.lines:
            mark_grid_list =  line.find_path()
            for spot in mark_grid_list:
                self.vent_map[spot.y][spot.x] += 1

    def __str__(self):
        final_grid = ''
        for row in range(0,self.y_bounds +1):
            for col in range(0,self.x_bounds +1):
                grid_spot = self.vent_map[row][col]
                if grid_spot > 0:
                    final_grid += str(grid_spot)
                else:
                    final_grid += '.'
            final_grid += '\n'
        return final_grid
    
    def score(self):
        count_val = sum(1 for col in chain.from_iterable(self.vent_map) if col > 1)
        return count_val

def main():
    input = read_input()
    vents = ventmap(input)
    #[print(l) for l in vents.lines]
    print(f'Max Size: {vents.x_bounds}, {vents.y_bounds}')
    start = time.time()
    print(vents)
    end = time.time()
    duration = end - start
    print(duration)

    print(vents.score())

def read_input():
    line_list = []
    temp_values = []
    inputFile = "input.txt"
    
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