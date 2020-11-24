#
# Main Driver that will ask if player wants to play or have AI play.
#
import Expectimax, game 


def main():

    print("Who will be playing this game? \n Human or AI? ")
    player=input()

    #if user pick ai as the player then the game would be play until the AI wins or lose.
    if(player == "AI"):
        
        #initiate the starting board and add a single random key tile that could be either
        #be a "4" or a "2" tile
        board=game.startingboard()
        game.add_new_key(board)

        game.print_board(board)

        # loop through the game condition until the Ai wins or loses the game
        while(True):
            
            game.print_board(board)
            x = input("Enter \'next\' for the Ai to commence an action: ")
            
            if x == "next":
                
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

    else :
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

main()
