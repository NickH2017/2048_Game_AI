#
# File stores the basic 2048 Game class
#
import random

# function initialize an empty 4*4 board grid and provided the list of command to input for game 
# and randomily position a '2' or '4' key on the board
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

#function add a random '2' or '4' key to the board that has a empty '0' key
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

#function return the state of the board wether or not if the game has won or not
def get_current_board(board):

    #loop through the board if a 2048 key exist
    for i in range(4):
        for x in range(4):
            if(board[i][x]== 2048):
                return "Won"
    #loop through wether there is a '0' still left in the tile
    for i in range(4):
        for j in range(4):
            if(board[i][j] == 0 ):
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
    #if all loop fail to find the condition of the game then it means that the current board is a lost
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

#function loop through the board and combined any tiles that have the same value then return board and a True indicated that it has been change. If no tiles
# have been found to merge then it return a false value and the board 
def merge(board):

    change = False

    for i in range(4):
        for j in range(3):

            if(board[i][j] == board[i][j+1] and board[i][j]!=0):

                board[i][j]=board[i][j]*2
                board[i][j+1] = 0

                change= True

    return board, change

# function return a new board that has it tiles been reverse from the given board
def reverse(board):

    new_board=[]
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[i][3-j])
    
    return new_board
#function perform a transpose process of a 2d array matrix, which is represented as the board
def transpose(board):
    new_board=[]

    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[j][i])

    return new_board
    
#function perfomed the action of moving the board left
def move_left(grid_matrix):

    new_grid_matrix , change1 = compress(grid_matrix)

    new_grid_matrix, change2 = merge(new_grid_matrix)

    change = change1 or change2

    new_grid_matrix, temp = compress(new_grid_matrix)

    return new_grid_matrix, change

#function perfomed the action of moving the board right
def move_right(grid_matrix):

    new_grid_matrix= reverse(grid_matrix)

    new_grid_matrix, change = move_left(new_grid_matrix)

    new_grid_matrix=reverse(new_grid_matrix)
    return new_grid_matrix, change

#function perfomed the action of moving the board up 
def move_up(grid_matrix): 
    
    new_grid_matrix = transpose(grid_matrix)

    new_grid_matrix, change = move_left(new_grid_matrix)

    new_grid_matrix = transpose(new_grid_matrix)
    return new_grid_matrix, change

#function perfomed the action of moving the board down 
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
