#
# Expectimax Algorithm Searches for the best 
# 
import game, math, sys, random

#functions

def weight_evaluation(board):
    
    #weight_val = 30
    var= 0
    weight_grid= []

    #create a weighted board to determine value positioning on the board
    weight_grid=[[0, 0, 0, 0],[0, 0, 0, 5],[0, 0, 5, 30],[0, 5, 30, 60]]

    #montonic heuristic 
    #loop through the board and determine it value by its position and the value of the key
    for i in range(3, -1, -1):
        for j in range(3,-1,-1):
            if(board[i][j]!=0):    
                if(board[i][j-1]!=0 or board[i-1][j]!=0):
                    if(board[i-1][j] >= board[i][j] or board[i][j-1] >= board[i][j]): 
                        var+=weight_grid[i][j]+(board[i][j]*2)

                    else:
                        var+=weight_grid[i][j] + (board[i][j])

    for i in range(3,0,-1):
        if(board[i][3]) != 0:
            if board[i-1][3] != 0:
                if(board[i-1][3] <= board[i][3]):
                    var+=weight_grid[i][3]+(board[i][3]*2)

                else:
                    var+=weight_grid[i][3]+(board[i][3])

    for j in range(3,0,-1):
        if(board[3][j]) != 0:
            if board[3][j-1] != 0:
                if(board[3][j-1] <= board[3][j]):
                    var+=weight_grid[3][j]+(board[3][j]*2)

                else : 
                    var+=weight_grid[3][j]+(board[3][j])

    penalty = 0
    for i in range(3, -1,-1):
        value = board[i][0]
        for j in range(3, -1,-1):
            penalty += abs(board[i][j] - value)+weight_grid[i][j]
    #print("Penalty: ", penalty)
    
    return var -penalty

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
        return board, temp
    elif action == 1:
        board, temp = game.move_down(board)
        return board, temp
    elif action == 2:
        board, temp = game.move_right(board)
        return board, temp
    elif action ==3:
        board, temp = game.move_left(board)
        return board, temp

# main Fucntions that are use to find the Expectimax

#recursive search function using Expectimax
def expectiminimax(board, node_type, depth):

    if game.get_current_board(board) == "Won":
        return sys.maxsize

    elif depth == 4:
        return weight_evaluation(board)

    elif game.get_current_board(board) == "game is lost":
        return 0
    
    elif node_type == "max":
        #print("hit for max")
        a=-100000
        
        for i in range(4):
            new_board= copy_board(board)
            new_board, flag =decision(new_board, i)
            #if flag:
            a = max(a, expectiminimax(new_board, "chance", depth+1) )
            #else:
            #    continue

    elif node_type == "chance":
        #print("hit for chance")
        a = 0
        count=0

        for i in range(4):
            for j in range(4):
                if board[i][j]==0:

                    new_board = copy_board(board)
                    new_board[i][j] = 2
                    count+=1

                    result = expectiminimax(new_board, "max", depth +1)

                    new_board[i][j] = 4
                    result2 = expectiminimax(new_board, "max", depth +1)

                    if result> result2:
                        a+=result
                    else:
                        a+=result2

        if count == 0:
            a = expectiminimax(board,"max" ,depth +1)
        #else :
        #   a = a/count
            
    #print("Score at depth: ", depth, " = ", a)
    return a

def ai_expectimax(board):

    decision_result=[]

    a = -100000

    for i in range(4):
            new_board= copy_board(board)
            new_board, flag  = decision(new_board, i)
            if flag:
                result = expectiminimax(new_board, "chance", 0+1)
                a = max(a, result)
                
                #game.print_board(new_board)
                #print(result)
                decision_result.append([result, i])
            else:
                continue

   # print(decision_result)
    for i in range(len(decision_result)):
        if a == decision_result[i][0]:
            return decision_result[i][1]
    return None