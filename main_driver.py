#
# Main Driver that will ask if player wants to play or have AI play.
#
import Expectimax, game 


def main():

    print("Who will be playing this game? \n Human or AI? ")
    player=input()

    #if user pick ai as the player then 
    if(player == "AI"):
        Expectimax.start()
    

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