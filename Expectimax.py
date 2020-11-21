#
# Expectimax Algorithm Searches for the best 
# 
import game, math, random

def weight_evaluation(board):
    
    weight_val=6
    var= 0
    weight_grid= []
    #create a weighted board to determine value positioning on the board
    for i in range(4):
        weight_grid.append([0]*4)
        
        for j in range(4):
            weight_grid[i][j]=pow(4, 6-(i))
        
        weight_val-=1

    #loop through the board and determine it value by its position and the value of the key
    for i in range(4):
        for j in range(4):
            if(board[i][j] != 0):
                var+=weight_grid[i][j] * board[i][j]

    return var

def add_key():
    x = random.randint(2,4)

    if x == 3:
        return x-1
    else :
        return x

#makes a new copy from board and return it
def copy_board(board):
    
    board_copy=[]
    for i in range(4):
        board_copy.append([0]*4)
        for j in range(4):
            board_copy[i][j]=board[i][j]
    
    return board_copy

def empty_tiles(board):
    count = 0 
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                count+=1
    return count

def decision(board, action):

    if action == 0:
        board, temp=game.move_up(board)
    elif action == 1:
        board, temp = game.move_down(board)
    elif action == 2:
        board, temp = game.move_right(board)
    elif action ==3:
        board, temp = game.move_left(board)


def expectiminimax(board, node_type, depth):

    if game.get_current_board(board) == "Won":
        return 100000

    elif depth == 4:
        return weight_evaluation(board)

    elif game.get_current_board(board) == "game is lost":
        return 0
    
    elif node_type == "max":

        a=100000
        
        for i in range(4):
            new_board= copy_board(board)
            decision(new_board, i)
            a = min(a, expectiminimax(new_board, "chance", depth+1) )
    
    elif node_type == "chance":
        a = 0
        count=0

        for i in range(4):
            for j in range(4):
                if board[i][j]==0:

                    new_board = copy_board(board)
                    new_board[i][j] = add_key()

                    count+=1
                    a = a + expectiminimax(new_board, "max", depth +1)

        a = a/count

    return a

def ai_expectimax(board):

    decision_result=[]

    a = 100000

    for i in range(4):
            new_board= copy_board(board)
            decision(new_board, i)
            a = min(a, expectiminimax(new_board, "chance", 0+1) )

            decision_result.append(a)

    for i in range(len(decision_result)):
        if a == decision_result[i]:
            return i