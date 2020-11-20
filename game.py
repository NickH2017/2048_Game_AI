#
# File stores the basic 2048 Game class
#
import random

# function initialize an empty 4*4 board grid and provided the list of command to input for game 
# and randomily position a '2' key on the board
def startingboard():

    board = []

    for i in range(4):
        board.append([0]*4)

    print("Available commands for the player: ")
    print("'w':  to move up")
    print("'s':  to move down")
    print("'a':  to move left")
    print("'d':  to move right")
    print("'quit: to quit the game")

    add_new_key(board)
    return board

#function add a random '2' key to the board that has a empty '0' key
def add_new_key(board) :

    row = random.randint(0, 3)
    column = random.randint(0, 3)

    while(board[row][column] != 0) : 
        row = random.randint(0, 3)
        column = random.randint(0, 3)
    
    x = random.randint(2,4)
    board[row][column]= x
    
    if x == 3:
        board[row][column]= x-1


def get_current_board(board):

    #loop through the board if a 2048 key exist
    for i in range(4):
        for x in range(4):
            if(board[i][x]== 2048):
                return "Won"
            elif(board[i][x]== 0):
                return "game not over"
    
    #loops check wether keys on the board has the same value
    for i in range(3):
        for j in range(3):
            if(board[i][j] == board[i+1][j] or board[i][j]==board[i][j+1]):
                return "game not over"

    for j in range(3): 
        if(board[3][j]== board[3][j + 1]): 
            return "game not over"
  
    for i in range(3): 
        if(board[i][3]== board[i + 1][3]): 
            return "game not over"

    return "game is lost"

#
def compress(board):

    change = False
    new_board=[]

    for i in range(4):
        new_board.append([0]*4)
    
    for i in range(4):
        pos=0

        for j in range(4):

            if(board[i][j] != 0):
                    new_board[i][pos]=board[i][j]

                    if(j != pos):
                        change= True
                    pos +=1
    return new_board, change

def merge(board):

    change = True

    for i in range(4):
        for j in range(3):

            if(board[i][j] == board[i][j+1] and board[i][j]!=0):

                board[i][j]=board[i][j]*2
                board[i][j+1] = 0

                change= True

    return board, change

def reverse(board):

    new_board=[]
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[i][3-j])
    
    return new_board

def transpose(board):
    new_board=[]

    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[j][i])

    return new_board
    
#function reponsible in intiating movement action for the game
def move_left(grid_matrix):

    new_grid_matrix , change1 = compress(grid_matrix)

    new_grid_matrix, change2 = merge(new_grid_matrix)

    change = change1 or change2

    new_grid_matrix, temp = compress(new_grid_matrix)

    return new_grid_matrix, change

def move_right(grid_matrix):

    new_grid_matrix= reverse(grid_matrix)

    new_grid_matrix, change = move_left(new_grid_matrix)

    new_grid_matrix=reverse(new_grid_matrix)
    return new_grid_matrix, change

def move_up(grid_matrix): 
    
    new_grid_matrix = transpose(grid_matrix)

    new_grid_matrix, change = move_left(new_grid_matrix)

    new_grid_matrix = transpose(new_grid_matrix)
    return new_grid_matrix, change

def move_down(grid_matrix):

    new_grid_matrix = transpose(grid_matrix)

    new_grid_matrix, change= move_right(new_grid_matrix)

    new_grid_matrix = transpose(new_grid_matrix)
    return new_grid_matrix, change

#function use for debugging purpose
def print_board(board):
    
    print("************")
    for i in range(4):
        print(board[i])
    
    print("************")

    return