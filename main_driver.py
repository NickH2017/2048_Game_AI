#
# Main Driver that will ask if player wants to play or have AI play.
#
import Expectimax, game
import GUI
import time

if __name__ == "__main__":
    
    while True:
        print("What interface would you like to use: \n1. Terminal \n2. GUI")
        gameOutput = input("Type 1 or 2:")

        try:
            gameOutput = int(gameOutput)
            if gameOutput == 1 or gameOutput == 2:

                if gameOutput == 2:
                    try:
                        import pygame
                        from pygame.locals import *
                    except:
                        print("Error: Pygame is not installed")
                        
                break
        except:
            print("Try Again. Choose 1 or 2")
            

    while True:
        print("Who will be playing this game?: \n1. Human \n2. AI")
        player = input("Type 1 or 2:")


        try:
            player = int(player)
            if player == 1 or player == 2:
                break
        except:
            print("Try Again. Choose 1 or 2")

    # Starts Pygame GUI with HUMAN control
    if(player == 1 and gameOutput == 2):
        new_game = GUI.gameGUI()
        new_game.play("HUMAN")

    # Starts Pygame GUI with AI control
    elif(player == 2 and gameOutput == 2):
        AIgame = GUI.gameGUI()
        AIgame.play("AI")
    
    #If user picks AI as the player then the game would be play until the AI wins or lose.
    elif(player == 2 and gameOutput == 1):
        
        #initiate the starting board and add a single random key tile that could be either
        #be a "4" or a "2" tile
        board=game.startingboard()
        game.add_new_key(board)

        game.print_board(board)

        # loop through the game condition until the Ai wins or loses the game
        while(True):
            
            game.print_board(board)
            x = input("Press 'Enter' key for the Ai to commence an action: ")
            
            if x == "":
                
                decision=Expectimax.ai_expectimax(board)

                if decision == 0:
                    board, flag = game.move_up(board)

                    current_status = game.get_current_board(board)
                    print(current_status)

                    if(current_status== "game not over"):
                        game.add_new_key(board)
                    else:
                        break
                elif decision == 1:
                    board, flag = game.move_down(board)

                    current_status = game.get_current_board(board)
                    print(current_status)

                    if(current_status== "game not over"):
                        game.add_new_key(board)
                    else:
                        break
                elif decision == 2 :
                    board, flag = game.move_right(board)

                    current_status = game.get_current_board(board)
                    print(current_status)

                    if(current_status== "game not over"):
                        game.add_new_key(board)
                    else:
                        break
                elif decision == 3:
                    board, flag = game.move_left(board)

                    current_status = game.get_current_board(board)
                    print(current_status)

                    if(current_status== "game not over"):
                        game.add_new_key(board)
                    else:
                        break
            elif x == "quit":
                break
            
            else: 
                print("Invalid command")

    elif player == 1 and gameOutput == 1:
        #begins to filled the board with the starting values and add a random key tile
        # that could either be "2" or "4"
        board = game.startingboard()
        game.add_new_key(board)

        #begins a while loop until the user stated to break it or the game is won
        while (True):
            
            #print out the current board for the user to see and decide which action to take
            game.print_board(board)
            x = input("Enter command: ")
            
            #statement check wether the user want the board to move the tiles up. When the action is perform
            #it will print out wether the game has been won or not. If the game is won it will commence a break to stop the while loop
            if(x == "w" or x == "W"):
                board, flag = game.move_up(board)

                current_status = game.get_current_board(board)
                print(current_status)

                if(current_status== "game not over"):
                    game.add_new_key(board)
                else:
                    break
            #statement check wether the user want the board to move the tiles down. When the action is perform
            #it will print out wether the game has been won or not. If the game is won it will commence a break to stop the while loop
            elif(x == "s" or x =="S"):
                 board, flag = game.move_down(board)

                 current_status = game.get_current_board(board)
                 print(current_status)

                 if(current_status =="game not over"):
                     game.add_new_key(board)
                 else:
                     break
            #statement check wether the user want the board to move the tiles right. When the action is perform
            #it will print out wether the game has been won or not. If the game is won it will commence a break to stop the while loop
            elif(x == "d" or x == "D"):
                 board, flag = game.move_right(board)

                 current_status = game.get_current_board(board)
                 print(current_status)

                 if(current_status =="game not over"):
                     game.add_new_key(board)
                 else:
                     break
            #statement check wether the user want the board to move the tiles left. When the action is perform
            #it will print out wether the game has been won or not. If the game is won it will commence a break to stop the while loop
            elif(x == "a" or x == "A"):
                 board, flag = game.move_left(board)

                 current_status = game.get_current_board(board)
                 print(current_status)

                 if(current_status =="game not over"):
                     game.add_new_key(board)
                 else:
                     break
            # statement check if the user want to quit from the game it would break out from the while loop and 
            elif( x == "quit"):
                print("quitting from the game")
                break
                
            #if player input a key that is not a valid move button for the game
            else :
                print("Invalid key")
    else:
        print("Error")

