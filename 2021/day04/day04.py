
class Board:
    cells = []
    rowCount = 0
    colCount = 0

    def __init__(self):
        self.cells = []
        self.rowCount = 0
        self.colCount = 0

    def __str__(self):
        #print the board with row / col under it
        retval = '\n'.join([" ".join( ["{:>2}".format(str(c)) for c in self.cells[i:i+self.colCount]]) for i in range(0,len(self.cells),self.colCount)])
        
        # retval = ''
        # for i, a in enumerate(self.cells):
        #     retval = retval + "{:>2}".format(a.value) + ' '
        #     if i % self.colCount == self.colCount - 1:
        #         retval = retval + '\n'

        retval = retval + f'\nBoard Columns: {self.colCount} Board Rows: {self.rowCount}'
        return retval

class Cell:
    value = -1
    marked = False

    def __init__(self, value, marked):
        self.value = value
        self.marked = marked

    def __str__(self):
        return self.value

def main():
    prng, boards = read_input()
    process_input(prng, boards)

def process_input(prng, boards):
    print(prng)
    [print(b) for b in boards]
    

def read_input():
    inputFile = "sample.txt"
    prng = []
    boards = []
    #grab the first line that acts as the RNG
    with open(inputFile) as f:
        prng = f.readline().strip('\n')

        #read into the void to skip the first blank line

        f.readline()
        current_board = Board()


        while (line := f.readline()):
            if len(line) <= 1 and len(current_board.cells) > 0 : #make sure it's not just a newline
                boards.append(current_board)
                current_board = Board()
                continue
            split_line = line.rstrip().split()
            if current_board.colCount <= 0:
                current_board.colCount = len(split_line)
            [current_board.cells.append(Cell(val, False)) for val in split_line ]
            current_board.rowCount = current_board.rowCount + 1

    return prng, boards

if __name__ == '__main__':
    main()
