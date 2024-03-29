import copy

class Board:
    cells = []
    rowCount = 0
    colCount = 0

    def __init__(self):
        self.cells = []
        self.rowCount = 0
        self.colCount = 0

    def check_if_winner(self):
        winner = False
        for r in range(0,self.rowCount):
            if winner == False:
                rowWinner = True
                for c in self.cells[(r*self.colCount):(r*self.colCount) + self.colCount]:
                    if c.marked == False:
                        rowWinner = False
                if rowWinner == True:
                    winner = True
        
        if winner == False:
            for col in range(0,self.colCount):
                if winner == False:
                    colWinner = True
                    for row in range(0,self.rowCount):
                        if self.cells[(row * self.colCount) + col].marked == False:
                            colWinner = False
                    if colWinner == True:
                        winner = True

        return winner

    def score_unmarked_cells(self):
        score = sum([int(c.value) for c in self.cells if c.marked == False])
        return score

    def __str__(self):
        #print the board with row / col under it
        retval = '\n'.join([" ".join( [f'{str(c):>2}' for c in self.cells[i:i+self.colCount]]) for i in range(0,len(self.cells),self.colCount)])
        
        # retval = ''
        # for i, a in enumerate(self.cells):
        #     retval +=  "{:>2} ".format(a.value)
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
        return str(self.value)

def main():
    prng, boards = read_input()
    process_bingo(prng, boards)

def process_bingo(prng, boards):
    #print(prng)
    #[print(b) for b in boards]

    # for each number of prng
    #   mark the spot if it exists in the board's cells
    #   Check if the board has a win yet
    #   Abort if a winner is selected
    # score routine

    has_winner = False
    winning_board = None
    winning_callout = 0
    winning_list = []
    gatekeeper_boards = []
    
    for callout in prng:
        for board in boards:
            for cell in board.cells:
                if cell.value == callout:
                    cell.marked = True
                    break
            is_winner = board.check_if_winner()
            if is_winner == True:
                if board not in gatekeeper_boards:
                    gatekeeper_boards.append(board)
                    deep_board = copy.deepcopy(board)
                    winning_list.append((deep_board, callout))
                #break
    
    winning_board, winning_callout = winning_list[len(winning_list) - 1]

    
    if winning_board != None:
        print("Winning board found!")
        print(winning_board)
        print(f'Winning Callout: {winning_callout}')
        final_score = calculate_final_score(winning_board, winning_callout)
        print(f'Your score: {final_score}')
    else:
        print("No winning board found.")

def calculate_final_score(board, callout):
    final_score = board.score_unmarked_cells() * callout
    return final_score

def read_input():
    inputFile = "input.txt"
    prng = []
    boards = []
    #grab the first line that acts as the RNG
    with open(inputFile) as f:
        temp_prng = f.readline().strip('\n')
        prng = list(map(int,temp_prng.split(',')))

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
            [current_board.cells.append(Cell(int(val), False)) for val in split_line ]
            current_board.rowCount = current_board.rowCount + 1

    return prng, boards

if __name__ == '__main__':
    main()
