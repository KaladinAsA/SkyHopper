import pygame
from setting import *
from pygame.image import load
from support import import_folder
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    '''player class that can jump and move left and right'''
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.flip = False
        # image
        self.image = load('graphics/elf/run/run_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (pos_x,pos_y))
        self.import_asset()
        self.status = 'run'
        self.hitbox = self.rect.inflate(20,25)
        # movment
        self.direction = Vector2()
        self.jumps = False
        self.jump_count = 0
        self.frame_index = 0
        self.fall_count = 0

    def import_asset(self):
        charechtor_path = 'graphics/elf/'
        self.animtion = {'run': [], 'jump': [], 'jump_prep': [],
                         'land': [], 'fall': [], 'idle': [], 'fall_left': [],
                         'jump_prep_left': []}
        
        for animation in self.animtion.keys():
            full_path = charechtor_path + animation
            self.animtion[animation] = import_folder(full_path,3,3)

    def get_status(self):
        '''getting player status by player action'''
        if self.direction.y == 1:
            self.status = 'fall'
        if self.rect.bottom >= HIGHT - 50:
            self.status = 'jump_prep'
        if self.direction.y == - JUMP_HIGHT:
            self.status = 'jump'
        
    def move(self):
        '''combine x and y with direction'''
        self.hitbox.x += self.direction.x
        self.hitbox.y += self.direction.y
        self.rect = self.hitbox
        
    def input(self):
        '''getting player input'''
        self.direction.x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x += PLAYER_SPEED
            self.flip = False
        elif keys[pygame.K_LEFT]:
            self.direction.x -= PLAYER_SPEED
            self.status = 'jump_prep_left'
        else:
            self.direction.x = 0
        self.move()

    def gravity(self):
        self.direction.y += min(1, self.fall_count / FPS * GRAVITY)
        self.fall_count += 1

    def collisoin(self):
        '''cheaking if player tuch the ground'''
        if self.hitbox.bottom >= HIGHT - 50:
            self.hitbox.bottom = HIGHT -50
            self.direction.y = - JUMP_HIGHT

    def animation(self):
        '''set frames by player status'''
        aniamtion = self.animtion[self.status]
        self.frame_index += 0.2
        if self.frame_index >= len(aniamtion):
            self.frame_index = 0
        self.image = aniamtion[int(self.frame_index)]

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image,self.flip,False),self.hitbox)
            
    def update(self):
        self.input()
        self.get_status()
        self.animation()
        self.gravity()
        self.collisoin()