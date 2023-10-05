import pygame,sys,json
from setting import *
from pygame.image import load
from sprites import Platform , Cloud, Tiles, Birds
from button import Button
import random
from player import Player
from menue import Text_Font

class Level:
    '''creating game levels that player can play'''
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.restart = False
        # lose 
        self.player_fall = False
        self.player_hit_bird = False
        # score
        self.high_score = 0
        self.score = 0
        self.score_increment = 1
        self.bird_score = 100
        self.player_lose = False
        self.load_high_score()
        # sprites 
        self.camera = Camera()
        self.platform_sprites = Camera()
        self.player_sprite = Camera()
        self.cload_sprite = Camera()
        self.floor_spriter = Camera()
        self.bird_sprite = Camera()
        # player
        self.player = Player(HIGHT - 200,WITDH//2)
        self.player_sprite.add(self.player)
        # paltform
        self.image = load('graphics/envirment/tiles/blue_2.png').convert_alpha()
        self.platform_levels()
        self.add_platform()
        # toggle
        self.player_alive = True
        # sound
        self.jump_sound = pygame.mixer.Sound('audio/jump.wav')
        self.jump_sound.set_volume(0.2)
        self.hit_sound = pygame.mixer.Sound('audio/hit.wav')
        self.hit_sound.set_volume(0.5)
        self.fall_sound = pygame.mixer.Sound('audio/fall_sound.wav')
        self.fall_sound.set_volume(0.5)
        # intial setup
        self.cloaud_timer = pygame.time.get_ticks()
        self.timer = pygame.time.get_ticks()
        self.load_cloauds()
        self.start_up_caluds(MAX_CLOUD)
        self.import_image()
        self.restart_button()
    
    def update_high_score(self):
        '''set high score on topest score of player'''
        if self.score > self.high_score:
            self.high_score = self.score
    
    def save_high_score(self):
        '''save high scor in json file'''
        with open("high_score.json", "w") as file:
            json.dump(self.high_score, file)
            print('svae')
        
    def load_high_score(self):
        '''loading last high score in game with json file'''
        try:
            with open("high_score.json", "r") as file:
                self.high_score = json.load(file)
                print('load')
        # if did not finde anything return 0
        except FileNotFoundError:
            self.high_score = 0
            print('o')
    
    def import_image(self):
        '''saving diffrent images in to memory'''
        self.grass_blue_2 = load(
            'graphics/border/grb_2.png').convert_alpha()
        self.panel = load(
            'graphics/button/panlle.png').convert_alpha()
        self.panel_withe = load(
            'graphics/button/white_panlle.png').convert_alpha()
        self.button_lomg = load(
            'graphics/button/buttonLong.png').convert_alpha()
        self.button_pressed = load(
            'graphics/button/buttonLong_pressed.png').convert_alpha()
        self.button_sq = load(
            'graphics/button/buttonSquare.png').convert_alpha()
        self.button_sq_pressed = load(
            'graphics/button/buttonSquare_pressed.png').convert_alpha()
        # elf
        self.dead_elf = load(
            'graphics/elf/dead.png').convert_alpha()
    # platform     
    def platform_levels(self):
        '''creating randome platform in diffren level of surface in start of game'''
        platform_level_1 = random.choice(
        [Platform(self.image,TILE_W,TILE_H,20,100),
        Platform(self.image,TILE_W,TILE_H,175,100),
        Platform(self.image,TILE_W,TILE_H,320,100),
        Platform(self.image,TILE_W,TILE_H,475,100)])
        
        platform_level_2 = random.choice(
        [Platform(self.image,TILE_W,TILE_H,20,250),
        Platform(self.image,TILE_W,TILE_H,175,250),
        Platform(self.image,TILE_W,TILE_H,320,250),
        Platform(self.image,TILE_W,TILE_H,475,250)])
        
        platform_level_3 = random.choice(
        [Platform(self.image,TILE_W,TILE_H,20,350),
        Platform(self.image,TILE_W,TILE_H,175,350),
        Platform(self.image,TILE_W,TILE_H,320,350),
        Platform(self.image,TILE_W,TILE_H,475,350)])
        
        platform_level_4 = random.choice(
        [Platform(self.image,TILE_W,TILE_H,20,500),
        Platform(self.image,TILE_W,TILE_H,175,500),
        Platform(self.image,TILE_W,TILE_H,320,500),
        Platform(self.image,TILE_W,TILE_H,475,500)])
        
        self.platform_sprites.add(platform_level_1)
        self.platform_sprites.add(platform_level_2)
        self.platform_sprites.add(platform_level_3)
        self.platform_sprites.add(platform_level_4)

    def add_platform(self):
        '''create platform if player grater than screen hieght'''
        platform_y = -50
        if self.player.hitbox.top < HIGHT:
            for platform in range(MAX_PLATFORM):
                # chose bettwen deiffrent x cordinate
                platform_level_1 = random.choice(
            [Platform(self.image,TILE_W,TILE_H,20,platform_y),
            Platform(self.image,TILE_W,TILE_H,175,platform_y),
            Platform(self.image,TILE_W,TILE_H,320,platform_y),
            Platform(self.image,TILE_W,TILE_H,475,platform_y)])
                # incress y codinte to get offset bettwen platform
                platform_y += -250
                self.platform_sprites.add(platform_level_1)
        
    # cloauds            
    def load_cloauds(self):
        self.clouad_1 = load(
            'graphics/envirment/clouds/Small Cloud 1.png').convert_alpha()
        self.clouad_2 = load(
            'graphics/envirment/clouds/Small Cloud 2.png').convert_alpha()
        self.clouad_3 = load(
            'graphics/envirment/clouds/Small Cloud 3.png').convert_alpha()
   
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
    # playe has lost and restart
    def dead_floor(self):
        '''adding floor for death ui'''
        floor = Tiles(self.grass_blue_2,5,5)
        floor.creat_multiple_tile(150, 520, 0, 5, 60)
  
    def show_death_ui(self):
        # elf
        elf = pygame.transform.scale(self.dead_elf,(100,100))
        # create panell
        w = self.panel.get_width()
        h = self.panel.get_height()
        panel = pygame.transform.scale(self.panel,(int(w*5),int(h*6)))
        withe_panel = pygame.transform.scale(self.panel_withe,(int(w*4),int(h*5)))
        # update     
        self.screen.blit(panel,(65,50))
        self.screen.blit(withe_panel,(120,100))
        self.screen.blit(elf,(250,420))
        self.dead_floor()
       
    def restart_button(self):
        '''adding button'''
        self.button_yes = Button(200,200,self.button_sq,self.button_sq_pressed,1) 
        self.button_no = Button(400,200,self.button_sq,self.button_sq_pressed,1) 

    def button_click(self):
        '''cheak if player click on yes button or no'''
        if self.button_yes.click:
            self.restarts()
        if self.button_no.click:
            self.back_to_menu = True

    def update_buttons(self):
        self.button_yes.update()
        self.button_no.update()
    
    def restarts(self):
        '''rest all varivle and start the game again'''
        # set the player positon bak to start
        self.player.rect.y = 700
        self.score = 0
        # changed th state of player
        self.player_lose = False
        # resaet all birds
        self.bird_sprite.empty()
        # rest the ways that player lose the game
        self.player_fall = False
        self.player_hit_bird = False
        # making sure restart trigger once
        if not self.restart:
            self.restart = True
               
    def add_text(self):
        '''display text on surface'''
        # loss
        you_lose_text = Text_Font('the poor elf is dead',35,(153, 119, 73) ,WITDH // 2 -  90, 125)
        you_lose_text.add_text()
        # restart
        restart_text = Text_Font('restart the game?', 30,TEXT_COLOR, WITDH // 2 -  60, 170)
        restart_text.add_text()
        # yes
        yes_text = Text_Font('YES',25,TEXT_COLOR,205,215)
        yes_text.add_text()
        # no
        no_text = Text_Font('NO',25,TEXT_COLOR,410,215)
        no_text.add_text()
        # score
        score = Text_Font(f'score: {self.score}', 40,(174, 194, 143),WITDH // 2 -  100,300)
        score.add_text()
        high_score = Text_Font(f'top score: {self.high_score}', 40,(0,0,0),WITDH//2-100,350)
        high_score.add_text()
    # collision   
    def collision(self):
        '''cheking if player collide wtih sprites'''
        # cheking bottom of player with platform
        if pygame.sprite.spritecollide(self.player,self.platform_sprites,False):
            if self.player.hitbox.bottom:
                self.player.direction.y = -JUMP_HIGHT
                self.jump_sound.play()
        # chek for player and birds
        if pygame.sprite.spritecollide(self.player,self.bird_sprite,False):
            self.hit_sound.play()
            print('dead')
          
    def screen_limit(self):
        '''limitation for player to dont go off screen'''
        if self.player.hitbox.right >= WITDH:
            self.player.hitbox.left = 0
        elif self.player.hitbox.left <= LEFT_LIMIT:
            self.player.hitbox.right = WITDH
                          
    # birds
    def adding_bird(self):
        '''adding birds when evere player rech the score and keep adding it'''
        y_pos = pygame.math.Vector2()[1]
        y_offset = 800
        # check if score rech the bird score to start creating bird
        if self.score >= self.bird_score:
            while len(self.bird_sprite) < MAX_BIRDS:
                # change the y pos every itrate
                y_pos += self.player.rect.top 
                # add offset to birds dont respawn close
                y_pos -= y_offset
                self.bird = Birds(0,y_pos,BIRD_SPEED)
                self.bird_sprite.add(self.bird)
                
    def kill_birds(self):
        '''destroyed birds when ever they bottom of screen'''
        for bird in self.bird_sprite:
            if bird.rect.bottom > self.bird_sprite.camera_rect.bottom:
                bird.kill()
          
    # score
    def add_score(self):
        '''add score if player reach the screen height'''
        if self.player.rect.top < self.platform_sprites.camera_rect.top:
            self.score += self.score_increment  
            
    def display_score(self):
        '''showing score to player'''
        if self.player_alive:
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {self.score}', True, (174, 194, 143))
            self.screen.blit(score_text, (10, 10))
    # running and looping
    def loop(self):
        '''event loop for menu'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.add_score()
        self.screen.fill((110, 153, 149))
        self.collision()
        self.screen_limit()
        self.display_score()
        # cloud
        self.cload_sprite.draw(self.screen)
        self.cload_sprite.update()
    
    def game_over(self):
        '''display game over section and methods to player'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.button_click()
        self.screen.fill((110, 153, 149))
        self.show_death_ui()
        self.update_buttons()
        self.add_text()
       
    def run(self):
        if not self.player_lose:
            # initial
            self.loop()
            self.cloud_respawn()
            # high score
            self.save_high_score()
            self.update_high_score()
            # platform
            self.platform_sprites.update()
            self.platform_sprites.coustom_draw(self.player)
            # player
            self.player_sprite.coustom_draw(self.player)
            self.player_sprite.update()
            # bird
            self.bird_sprite.update()
            self.adding_bird()
            self.kill_birds()
            self.bird_sprite.coustom_draw(self.player)
            # cheking if player fall out of screen or hit a bird
            if self.player.hitbox.bottom >= self.player_sprite.camera_rect.bottom:
                self.fall_sound.play()
                self.player_fall = True
            elif pygame.sprite.spritecollide(self.player,self.bird_sprite,False):
                self.hit_sound.play()
                self.player_hit_bird = True

    # other class
class Camera(pygame.sprite.Group):
    '''changing camera view'''
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_hight = self.screen.get_size()[1] // 2 
        # box camer
        self.camera_border = {'left': 100, 'right': 100, 'top': 50, 'bottom': 50}
        l = self.camera_border['left']
        t = self.camera_border['top']
        w = self.screen.get_size()[0] - (self.camera_border['left'] + self.camera_border['right'])
        h = self.screen.get_size()[1] - (self.camera_border['top'] + self.camera_border['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)
    
    def box_target_camera(self,target):
        '''camera that draw a box and when rech on it will move'''
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom
        # showing how much target can see and subtract 50 for more views
        self.offset.y = self.camera_rect.top - self.camera_border['top'] -220
        
    def coustom_draw(self,player):
        '''drawin every elemnt in sprite by player rect'''
        # offset
        self.box_target_camera(player)
        # getting all sprites
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image,offset_pos)
        
