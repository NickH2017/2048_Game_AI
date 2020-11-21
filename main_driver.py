#
# Main Driver that will ask if player wants to play or have AI play.
#
import Expectimax, game 


def main():

    print("Who will be playing this game? \n Human or AI? ")
    player=input()

    #if user pick ai as the player then 
    if(player == "AI"):
        board=game.startingboard()
        game.add_new_key(board)

        game.print_board(board)

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
        
        board = game.startingboard()
        game.add_new_key(board)

        while (True):
            
            game.print_board(board)
            x = input("Enter command: ")

            if(x == "w" or x == "W"):
                board, flag = game.move_up(board)

                current_status = game.get_current_board(board)
                print(current_status)

                if(current_status== "game not over"):
                    game.add_new_key(board)
                else:
                    break
            elif(x == "s" or x =="S"):
                 board, flag = game.move_down(board)

                 current_status = game.get_current_board(board)
                 print(current_status)

                 if(current_status =="game not over"):
                     game.add_new_key(board)
                 else:
                     break
            
            elif(x == "d" or x == "D"):
                 board, flag = game.move_right(board)

                 current_status = game.get_current_board(board)
                 print(current_status)

                 if(current_status =="game not over"):
                     game.add_new_key(board)
                 else:
                     break
            
            elif(x == "a" or x == "A"):
                 board, flag = game.move_left(board)

                 current_status = game.get_current_board(board)
                 print(current_status)

                 if(current_status =="game not over"):
                     game.add_new_key(board)
                 else:
                     break
            
            elif( x == "quit"):
                print("quitting from the game")
                break
            
            else :
                print("Invalid key")

main()