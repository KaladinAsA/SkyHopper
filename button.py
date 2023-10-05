import pygame
from setting import *
from pygame.mouse import get_pos as mouse_pos

class Button:
    """generating button with image"""
    
    def __init__(self, x, y, image, image_2 = None, scale = 0):
        # display setup
        pygame.init()
        self.screen = pygame.display.get_surface()
        # getting image w,h
        width = image.get_width()
        height = image.get_height()
        # image set_up
        self.image = pygame.transform.scale(image, (int(width* scale), int(height* scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        # image_2 set_up
        self.image_2 = pygame.transform.scale(image_2, (int(width* scale), int(height* scale)))
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.topleft = (x,y)
        # check the mouse
        self.click = False
     
    def draw(self):
        '''draw button images'''
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        # if self.click is True show diffrent image
        if self.click:
            self.screen.blit(self.image_2, (self.rect_2.x, self.rect_2.y))
            
    def get_presede(self):
        '''check for user mouse clicked and changing it to True or False'''
        pos = mouse_pos()
        user = pygame.mouse.get_pressed()[0]
        # if mouse contact with rect
        if self.rect.collidepoint(pos):
            if user:
                self.click = True
            else:
                self.click = False
                      
    def update(self):
        '''updatin button methods'''
        self.draw()
        self.get_presede()
        