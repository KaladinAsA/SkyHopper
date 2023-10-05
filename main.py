import pygame
from setting import *
from menue import Menue
from pygame.image import load
from level import Level

class Main:
    '''A class to run all classes'''
    def __init__(self):
        # display set up
        pygame.mixer.pre_init(44100,-16,2,2048)
        pygame.mixer.init(buffer=512)
        pygame.init()
        self.screen = pygame.display.set_mode((WITDH, HIGHT))
        pygame.display.set_caption('SkyHopper')
        self.clock = pygame.time.Clock()
        self.game_state = 'main_menu'
        # menue setup
        self.menu = Menue()
        self.game_over = False
        self.level = Level()
        # mouse cursur changing
        cursur_image = load(
            'graphics/menue/cursorGauntlet_grey.png').convert_alpha()
        cursur = pygame.cursors.Cursor((0,0),cursur_image)
        pygame.mouse.set_cursor(cursur)
                  
    def run(self):
        while True:
            # cheacking diffrent state of game 
            # menu
            if self.game_state == 'main_menu':
                self.menu.run()
                if self.menu.button_start.click:
                    self.game_state = 'playing'
            # playing
            elif self.game_state == 'playing' and not self.game_over:
                self.level.run()
                # cheak if player fall of the screen or hit a bird if that the case he lose
                if self.level.player_fall or self.level.player_hit_bird:
                    self.level.player_lose = True
                    # making sure game over triger once
                    if not self.game_over:
                        self.game_over = True
                    self.game_state = 'game_over'
            # game over
            elif self.game_state == 'game_over' and self.game_over:
                # show game over state in surface
                    self.level.game_over()
                    if self.level.restart:
                    # making sure to set back game_over to False
                        if self.game_over:
                            self.game_over = False
                        self.game_state = 'playing'

            # updating window and FPS
            pygame.display.update()
            self.clock.tick(FPS)
    
if __name__ == '__main__':
    main = Main()
    main.run()
