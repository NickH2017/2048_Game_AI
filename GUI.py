import pygame
import Expectimax
import game
from pygame.locals import *
import time

tileColors = {
    0: (200, 200, 200),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (250, 123, 92),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (236, 199, 80),
    512: (239, 196, 64),
    1024: (227, 186, 19),
    2048: (236, 196, 2),
    4096: (102, 209, 157)
}

# Creates a game in pygame
class gameGUI:

    def __init__(self):
        self.board = game.startingboard()
        self.running = True
        #self.event= -1

        pygame.init()
        pygame.display.set_caption("2048 Game")
        pygame.font.init()
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
        self.screen = pygame.display.set_mode((600,600))

    def draw_board(self):

        self.screen.fill((190, 170, 160))

        for i in range(4):
            for j in range(4):
                tile = self.board[i][j]

                spacing = 10

                x = j * 600 // 4 + 10
                y = i * 600 // 4 + 10
                w = 600 // 4 - 2 * 10
                h = 600 // 4 - 2 * 10

                pygame.draw.rect(self.screen,
                                 tileColors[tile],
                                 pygame.Rect(x,y,w,h),
                                 border_radius=30)
                if tile == 0:
                    continue
                text_surface = self.font.render(f'{tile}', True, (0,0,0))
                text_rect = text_surface.get_rect(center=(x + w / 2,
                                                          y + h / 2))
                self.screen.blit(text_surface, text_rect)

    def won(self):

        self.draw_board()
        pygame.display.flip()

        text = self.font.render('WIN', True, (0, 0, 0))
        textBox = text.get_rect()
        textBox.center = (600 // 2, 600 // 2) 
  
        #self.screen.fill((255,255,255)) 
        self.screen.blit(text,textBox)

        #self.draw_board()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()


    def lost(self):

        text = self.font.render('GAME OVER', True, (0, 0, 0))
        textBox = text.get_rect()
        textBox.center = (600 // 2, 600 // 2) 
  
        #self.screen.fill((255,255,255)) 
        self.screen.blit(text,textBox)

        #self.draw_board()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()


    def play(self, player):

        if player == "AI":

            print("Ready? Press space bar to continue.")
            space = False
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.running = False
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_SPACE:
                            space = True
                            break
                
                if space:
                    break
                    
        
        while self.running:

            self.draw_board()
            pygame.display.update()
            pygame.display.flip()
            #cmd = -1

            tempboard = Expectimax.copy_board(self.board)

            if player == "AI":
                cmd = Expectimax.ai_expectimax(tempboard)
            elif player == "HUMAN":

                # Keyboard input commands
                cmd = 'g'
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            self.running = False
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_UP:
                                cmd = 'u'
                                break
                            elif event.key == K_DOWN:
                                cmd = 'd'
                                break
                            elif event.key == K_LEFT:
                                cmd = 'l'
                                break
                            elif event.key == K_RIGHT:
                                cmd = 'r'
                                break
                            elif event.key == K_q or event.key == K_ESCAPE:
                                self.running = False
                                pygame.quit()
                                exit()
                    
                    if cmd == 'u' or cmd == 'd' or cmd == 'l' or cmd == 'r':
                        break

                
            if cmd == 'u' or cmd == 0:
                tempboard, flag = game.move_up(tempboard)

                current_status = game.get_current_board(tempboard)
                print(current_status)

                if(current_status == "game not over"):
                    game.add_new_key(tempboard)
                elif current_status == "Won":
                    self.won()
                else:
                    self.lost()
                        
            elif cmd == 'd' or cmd == 1:
                tempboard, flag = game.move_down(tempboard)

                current_status = game.get_current_board(tempboard)
                print(current_status)

                if(current_status == "game not over"):
                    game.add_new_key(tempboard)
                elif current_status == "Won":
                    self.won()
                else:
                    self.lost()
                
            elif cmd == 'r' or cmd == 2:
                tempboard, flag = game.move_right(tempboard)

                current_status = game.get_current_board(tempboard)
                print(current_status)

                if(current_status =="game not over"):
                    game.add_new_key(tempboard)
                elif current_status == "Won":
                    self.won()
                else:
                    self.lost()
                
            elif cmd == 'l' or cmd == 3:
                tempboard, flag = game.move_left(tempboard)

                current_status = game.get_current_board(tempboard)
                print(current_status)

                if(current_status == "game not over"):
                    game.add_new_key(tempboard)
                elif current_status == "Won":
                    self.won()
                else:
                    self.lost()
            else:
                self.lost() 
            self.board = Expectimax.copy_board(tempboard)

# TEST CODE FOR TA         
#new_game = gameGUI()
#new_game.play("AI")