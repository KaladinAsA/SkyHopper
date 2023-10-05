import pygame,sys
from setting import *
from pygame.image import load
from button import Button
from support import import_folder 
import random
from random import randint
from sprites import Cloud, Animation, Tiles

class Menue:
    '''A menue class to chosse betteewn diffrent aspect of the game'''
    def __init__(self):
        # display set_up
        self.screen = pygame.display.get_surface()
        self.active = True
        # sprites group
        self.animation_sprite = pygame.sprite.Group()
        self.cload_sprite = pygame.sprite.Group()
        # initials
        self.cloaud_timer = pygame.time.get_ticks()
        self.animations()
        self.load_tiles()
        self.load_buttons()
        self.load_cloauds()
        self.start_up_caluds(MAX_CLOUD)
        self.button()
        self.texts()
        
    def load_tiles(self):
        '''load tiles images'''
        self.grass_blue_1 = load(
            'graphics/border/grb_1.png').convert_alpha()
        self.grass_blue_2 = load(
            'graphics/border/grb_2.png').convert_alpha()
        self.grass_blue_3 = load(
            'graphics/border/grb_3.png').convert_alpha()
        self.flower_1 = load(
            'graphics/border/flower_1.png').convert_alpha()
        self.blue_tree = load(
            'graphics/border/blue_tree.png').convert_alpha()
        self.stone_1 = load(
            'graphics/border/stone_1.png').convert_alpha()
        self.root_1 = load(
            'graphics/border/root_1.png').convert_alpha()
        self.root_2 = load(
            'graphics/border/root_2.png').convert_alpha()
        self.box = load(
            'graphics/border/box.png').convert_alpha()
        self.tresure = load(
            'graphics/border/tresure_1.png').convert_alpha()
        self.point_marker = load(
            'graphics/border/point_marker.png').convert_alpha() 
    
    def load_buttons(self):
        '''load button images'''
        # button
        self.button_long = load(
            'graphics/button/buttonLong.png').convert_alpha()
        self.button_long_brown = load(
            'graphics/menue/buttonLong_brown_pressed.png').convert_alpha()
        self.button_square = load(
            'graphics/button/buttonSquare.png').convert_alpha()
        # button_pressed
        self.button_pressed = load(
            'graphics/button/buttonLong_pressed.png').convert_alpha()
        self.button_square_prd = load(
            'graphics/button/buttonSquare_pressed.png').convert_alpha()
    
    def load_cloauds(self):
        self.clouad_1 = load(
            'graphics/envirment/clouds/Small Cloud 1.png').convert_alpha()
        self.clouad_2 = load(
            'graphics/envirment/clouds/Small Cloud 2.png').convert_alpha()
        self.clouad_3 = load(
            'graphics/envirment/clouds/Small Cloud 3.png').convert_alpha()
    # clouds      
    def start_up_caluds(self,amount):
        '''creating amount of cloaud'''
        for i in range(amount):
           cloauds = random.choice(
               [Cloud(self.clouad_1, 0,WITDH, 10,HIGHT-150,True),
                Cloud(self.clouad_2, 0,WITDH, 10,HIGHT- 150,True),
                Cloud(self.clouad_3, 0,WITDH, 10,HIGHT-150,True)])
           self.cload_sprite.add(cloauds)
           
    def add_clouds(self):
        '''create and constently add cloud in time'''
        clouds = random.choice(
            [Cloud(self.clouad_1,670,700,10,HIGHT-150,True),
            Cloud(self.clouad_2,640,700,10,HIGHT-150,True),
            Cloud(self.clouad_3,630,660,300,HIGHT-150,True)])
        self.cload_sprite.add(clouds)
        self.cloaud_timer = pygame.time.get_ticks()

    def cloud_respawn(self):
        '''after 2 sec respawn cloud'''
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.cloaud_timer > 2000:
            self.add_clouds()
        
    def border(self):
        '''creating and drawing simple border'''
        # top layers
        border_top_1 = pygame.Rect(0, 0, WITDH, 50)
        border_top_2 = pygame.Rect(10, 10, WITDH - 20, 30)
        border_top_3 = pygame.Rect(20, 20, WITDH - 40, 10)
        # drawing top layers BY ORDER
        pygame.draw.rect(self.screen, (59, 39, 21), border_top_1)
        pygame.draw.rect(self.screen, (128, 91, 59), border_top_2, width= 5)
        pygame.draw.rect(self.screen, (163, 137, 114), border_top_3)
    
    # Tiles        
    def add_tile(self):
        '''creating single tile to fill gaps or...'''
        # tree
        tile_tree = Tiles(self.blue_tree, 4, 4.7)
        tile_tree.creat_tile(200, 50)
        # corner left tile
        tile_corner_l = Tiles(self.grass_blue_1, 4, 4)
        tile_corner_l.creat_tile(0,HIGHT - 60)
        #corner right tile
        tile_corner_r = Tiles(self.grass_blue_3, 4, 4)
        tile_corner_r.creat_tile(WITDH - 60,HIGHT - 60)
        # stone
        tile_stone = Tiles(self.stone_1, 4, 4)
        tile_stone.creat_tile(50, HIGHT - 90)
        # point
        tile_point = Tiles(self.point_marker,4,4)
        tile_point.creat_tile(70, HIGHT - 110)
        # flower
        tile_flower = Tiles(self.flower_1, 5, 5)
        tile_flower.creat_tile(100,HIGHT - 90)
        # roots
        tile_root_1 = Tiles(self.root_1, 4, 4)
        tile_root_1.creat_tile(0,0)
        tile_root_2 = Tiles(self.root_2, 4, 4)
        tile_root_2.creat_tile(0,0)
        # box
        tile_box = Tiles(self.box, 4, 4)
        tile_box.creat_tile(275, HIGHT - 108)
        # tresure
        tile_tresure = Tiles(self.tresure, 4, 4)
        tile_tresure.creat_tile(360,HIGHT - 105)
        
    def add_multi_tile(self):
        '''creat rows or colms of tiles'''
        rows = Tiles(self.grass_blue_2, 4, 4)
        rows.creat_multiple_tile(60, HIGHT - 60, 0, 8, 60)
        
    # Button
    def button(self):
        '''creating button instense'''
        # start        
        self.button_start = Button(
            x = WITDH // 2 -  100,
            y = 220,
            image = self.button_long,
            image_2 = self.button_pressed,
            scale = 1)
        # setting
        self.button_setting = Button(
            x = WITDH // 2 - 100,
            y = 380,
            image = self.button_long,
            image_2 = self.button_pressed,
            scale = 1)       
        # skin
        self.button_skin = Button(
            x = WITDH // 2 - 100,
            y = 300,
            image = self.button_long,
            image_2 = self.button_pressed,
            scale = 1)
        # exit
        self.button_exit = Button(
            x = WITDH - 40,
            y = 10,
            image = self.button_square,
            image_2 = self.button_square_prd,
            scale = 0.8)
        
        self.button_restart = Button(
            x = WITDH // 2 -  100,
            y = 220,
            image = self.button_long,
            image_2 = self.button_pressed,
            scale = 1)
        
    def update_buttons(self):
        '''drawing diffrent buttons and updating'''
        self.button_start.update()
        self.button_setting.update()
        self.button_skin.update()
        self.button_exit.update()
             
    def button_clicked(self):
        '''cheaking if any buttons was clicked'''
        # closing game with exit button
        if self.button_exit.click:
            pygame.quit()
            sys.exit()
        # starting game 
        if self.button_start.click:
            print('game has started')
            self.active = False
        # opening setting
        if self.button_setting.click:
            print('setting has opened')
        # opening skin menue
        if self.button_skin.click:
            print('skin hass opened')
  
    def texts(self):
        '''add text on display'''
        #start
        self.start_text = Text_Font(
            'start', 40, TEXT_COLOR, WITDH // 2 -  35, 230)
        # setting
        self.setting_text = Text_Font(
            'setting', 40, TEXT_COLOR, WITDH // 2 - 50, 390)
        # skin
        self.skin_text = Text_Font(
            'skin', 40, TEXT_COLOR, WITDH // 2 - 35, 310 )
        # exit
        self.exit_text = Text_Font(
            'exit', 20, (214, 36, 36), WITDH - 35, 20 )
  
    def draw_text(self):
        '''drawing difrrent texts instense'''
        self.start_text.add_text()
        self.setting_text.add_text()
        self.skin_text.add_text()
        self.exit_text.add_text()
  
    def animations(self):
        '''difrents animations instense'''
        self.elf_animate = Animation(
            224, 567, 'graphics/elf/run',3 , 3, 0.2)
        self.swooh = Animation(
            200, HIGHT - 75, 'graphics/swoosh', 1, 0.5, 0.1, True)
        
    def sprite_animated(self):
        '''add animated object to animation sprite'''
        self.animation_sprite.add(self.swooh)
        self.animation_sprite.add(self.elf_animate)
        self.animation_sprite.draw(self.screen)
        self.animation_sprite.update()
    # Runing and looping 
    def loop(self):
        '''event loop for menu'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.button_clicked()
        self.screen.fill((110, 153, 149))
        self.cload_sprite.draw(self.screen)
        self.cload_sprite.update()
        self.border()
           
    def run(self):
        # evrithing should run after loop!
        self.loop()
        self.cloud_respawn()
        self.add_tile()
        self.add_multi_tile()
        self.sprite_animated()
        self.update_buttons()
        self.draw_text()
        
class Text_Font:
    '''A class to rendering and write texts to surface'''
    def __init__(self, text, size, color, x, y):
        # intial pygame,other wise class wont work!
        self.screen =  pygame.display.get_surface()
        # text and font setup
        self.text = text
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        # font style
        self.text_font = pygame.font.SysFont(None, self.size)

    def add_text(self):
        '''rendering the text and setting the color'''
        text = self.text_font.render(self.text, True, self.color)
        # blit text into surface
        self.screen.blit(text, (self.x, self.y))
        