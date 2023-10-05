import pygame
from setting import *
from support import import_folder
from pygame.image import load
import random

class Platform(pygame.sprite.Sprite):
    '''generating randome platform on surface'''
    def __init__(self, image, width, height, x, y):
        super().__init__()
        self.screen = pygame.display.get_surface()
        # image setup
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(
            image,(int(self.width* width), int(self.height* height)))
        self.rect = self.image.get_rect(topleft = (x,y))
        
class Cloud(pygame.sprite.Sprite):
    '''generating randome cloauds'''
    def __init__(
        self, image, start_x , stop_x, start_y, stop_y,move = False):
        super().__init__()
        self.move = move
        self.image = image
        offset_x = 100
        offset_y = 70
        # random cordinate
        self.pos_x = random.randrange(
            start_x,stop_x)
        self.pos_y = random.randrange(
            start_y,stop_y - 150)
        # rect
        self.rect = self.image.get_rect(
            topleft = (self.pos_x + offset_x,
                       self.pos_y + offset_y))      
        
    def update(self):
        if self.move:
            self.rect.x -= CLOAUD_SPEED
            # destroyd cload
            if self.rect.x <- 300:
                self.kill()

class Animation(pygame.sprite.Sprite):
    '''creating animated objects'''
    def __init__(self,
                pos_x, pos_y,assest,
                width, height, speed,
                flip_x =False, flip_y =False):
        super().__init__()
        # getting path and importing it as list
        self.sprites = import_folder(
            assest, width, height, flip_x, flip_y)
        # animations set_up
        self.current = 0
        self.image = self.sprites[self.current]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.speed = speed
        
    def update(self):
        self.current += self.speed
        if self.current >= len(self.sprites):
            self.current = 0
        self.image = self.sprites[int(self.current)]   

class Tiles(pygame.sprite.Sprite):
    '''creating collidebale tiles like walls and floor'''
    def __init__(self, image, width, height):
        super().__init__()
        self.screen = pygame.display.get_surface()
        # image setup
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(
            image,(int(self.width* width), int(self.height* height)))
        self.rect = self.image.get_rect()
        
    def creat_tile(self, x, y):
        '''create single tile and flexible with while loop'''
        self.screen.blit(self.image, (x , y))
    
    def creat_multiple_tile(
        self, x, y, amount = 0,
        max_amount = 1, x_offset = 0, 
        y_offset = 0):
        '''creat numbers of tiles with for loop'''
        for i in range(amount, max_amount):
            self.screen.blit(self.image, (x, y))
            # adding offset to split tiles
            x += x_offset
            y += y_offset
    
class Birds(pygame.sprite.Sprite):
    '''creating birds to move left and right on surface'''
    def __init__(self,x,y,bird_speed):
        super().__init__()
        self.screen = pygame.display.get_surface()
        # imaes
        self.image = load('graphics/envirment/birds/left/bird_L1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))
        self.frame_index = 0
        self.import_bird_assest()
        self.status = 'left'
        # move
        self.bird_speed = bird_speed
        self.directin = pygame.math.Vector2(self.bird_speed,0)
        
    def import_bird_assest(self):
        '''getting bird images'''
        charechtor_path = 'graphics/envirment/birds/'
        self.animtion = {'right': [], 'left': []}
        for animation in self.animtion.keys():
            full_path = charechtor_path + animation
            self.animtion[animation] = import_folder(full_path,3,3)
        
    def moves(self):
        '''changing bird direction when ever hit the width'''
        self.rect.x += self.directin.x
        # move right
        if self.rect.x >= WITDH - 10:
            self.directin.x -= self.bird_speed
            self.status ='right'
        # move left
        elif self.rect.x <= 0 -20:
            self.directin.x += self.bird_speed
            self.status = 'left'
       
    def animation(self):
        '''set frames by bird status'''
        aniamtion = self.animtion[self.status]
        self.frame_index += 0.2
        if self.frame_index >= len(aniamtion):
            self.frame_index = 0
        self.image = aniamtion[int(self.frame_index)]

    def update(self):
        self.moves()
        self.animation()
        
            

        