
import time

'''
1. All libraries removed
2. data from https://datahub.io/machine-learning/tic-tac-toe#data
3. min max algorithym 
4. This is currently reading from a 3 BY 3 SYSTEM,  but should be easy to expand
5. https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/ this website helped a lot
6. https://www.youtube.com/watch?v=trKjYdBASyQ was also helpful

'''

n = 0

with open(r'D:\AllImportantStuff\AllUWMadisonStuff\UWMadisonDiscussionSheetsAndEverything\CompSci\p6\tic-tac-toe.csv') as f:
    data = list(f)[1:]

board = {}
rowColSize = 0
n = 0
maxPlayer, minPlayer, empty = 'x', 'o', 'b'

for d in data: # for any size this works
    l = d.strip('\n').split(',')
    rowColSize = int( (len(l) - 1) ** (1/2) )

    for x in l:
        board[x] = {}

        for boardNums in range(rowColSize):
            numberInDict = int( boardNums )
            board[x][boardNums] = {}

            for individualNums in range(rowColSize):
                individualNumSpecific = int( (boardNums * rowColSize) + individualNums)
                board[x][boardNums][individualNums] = l[individualNumSpecific]

        board[x][rowColSize-1][rowColSize] = l[(rowColSize ** 2)]
        #print(board[x]) # note last number is the postive or negitive 

def movesLeft(board):
    for row in range(rowColSize):
        for col in range(rowColSize):
            if(board[row][col]) == 'b':
                return True
    return False



def checkWinner(board):
    for row in range(rowColSize):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]): #for a 3 by 3 system
            if (board[row][0] == maxPlayer) :
                return 10000
            elif (board[row][0] == minPlayer) :
                return -10000

    #columns
    for col in range(3) :
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
            if (board[0][col] == maxPlayer) :
                return 10
            elif (board[0][col] == minPlayer) :
                return -10


    #diagonal
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
     
        if (board[0][0] == maxPlayer) :
            return 10
        elif (board[0][0] == minPlayer) :
            return -10
 
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
     
        if (board[0][2] == maxPlayer) :
            return 10
        elif (board[0][2] == minPlayer) :
            return -10
    
    return 0

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()




def max_alpha_beta(isMaxPlayer, alpha, beta):
        maxv = -2
        px = None
        py = None

        checkWinner


        for row in range(rowColSize):
            for col in range(rowColSize):
                if self.current_state[row][col] == '.':
                    self.current_state[row][col] = 'O'
                    (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv

        return (maxv, px, py)




def min_alpha_beta(self, alpha, beta):

        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for row in range(rowColSize):
            for col in range(rowColSize):
                if self.current_state[row][row] == '.':
                    self.current_state[col][col] = 'X'
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)


def play_alpha_beta(self):
     while True:
        self.draw_board()
        self.result = self.is_end()

        if self.result != None:
            if self.result == 'X':
                print('The winner is X!')
            elif self.result == 'O':
                print('The winner is O!')
            elif self.result == '.':
                print("It's a tie!")


            self.initialize_game()
            return

        if self.player_turn == 'X':

            while True:
                start = time.time()
                (m, qx, qy) = self.min_alpha_beta(-2, 2)
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                px = int(input('Insert the X coordinate: '))
                py = int(input('Insert the Y coordinate: '))

                qx = px
                qy = py

                if self.is_valid(px, py):
                    self.current_state[px][py] = 'X'
                    self.player_turn = 'O'
                    break
                else:
                    print('The move is not valid! Try again.')

        else:
            (m, px, py) = self.max_alpha_beta(-2, 2)
            self.current_state[px][py] = 'O'
            self.player_turn = 'X'