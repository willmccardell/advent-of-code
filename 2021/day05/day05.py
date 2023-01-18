from parse import *
import time

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

    def is_straight(self):
        return self.start_point.x == self.end_point.x or self.start_point.y == self.end_point.y

    def is_point_along(self,p):
        return (p.x >= self.start_point.x and p.x <= self.end_point.x and \
                p.y >= self.start_point.y and p.y <= self.end_point.y) or \
                (p.x >= self.start_point.x and p.x <= self.end_point.x and \
                p.y <= self.start_point.y and p.y >= self.end_point.y) or \
                (p.x <= self.start_point.x and p.x >= self.end_point.x and \
                p.y >= self.start_point.y and p.y <= self.end_point.y) or \
                (p.x >= self.start_point.x and p.x <= self.end_point.x and \
                p.y >= self.start_point.y and p.y <= self.end_point.y)     

    def dumbly_find_path(self):
        path_list = []
        path_list.append(self.start_point)
        path_list.append(self.end_point)
        direction_x = self.end_point.x - self.start_point.x 
        direction_y = self.end_point.y - self.start_point.y

        impulse_x = 1
        impulse_y = 1

        if direction_x < 0:
            impulse_x = -1

        if direction_y < 0:
            impulse_y = -1

        for dx in range(0,direction_x, impulse_x ):
            dumb_point = point(self.start_point.x + dx, self.start_point.y)
            if dumb_point != self.start_point:
                if self.is_point_along(dumb_point):
                    path_list.append(dumb_point)

        for dy in range(0,direction_y, impulse_y):
            dumb_point = point(self.start_point.x, self.start_point.y + dy)
            if dumb_point != self.start_point:
                if self.is_point_along(dumb_point):
                    path_list.append(dumb_point)


        return path_list

    def path(self):
        return [point(0,0)]

    def max_x_cardinality(self):
        return max(self.start_point.x, self.end_point.x)
    
    def max_y_cardinality(self):
        return max(self.start_point.y, self.end_point.y)

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
            if line.is_straight():
                mark_grid_list =  line.dumbly_find_path()
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

    def dumb_map(self):
        final_grid = ''
        for row in range(0,self.y_bounds + 1): 
            for col in range(0,self.x_bounds + 1):
                grid_spot_value = '.'
                p = point(col,row)
                grid_spot_count = 0
                for line in self.lines:
                    if line.is_straight():
                        if line.is_point_along(p):
                            grid_spot_count += 1
                if grid_spot_count > 0:
                    grid_spot_value = str(grid_spot_count)
                final_grid += grid_spot_value
            final_grid += '\n'
        return final_grid

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

# remove lines that aren't straight
def purge_input(input):
    return list(filter(lambda x: x.is_straight(),input))

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