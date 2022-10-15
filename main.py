from tkinter import Toplevel
import pygame
from random import randint, choice
from sys import *
from random import *
import numpy as np

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'top':
            enemigo_top_1 = pygame.image.load('assets/enemigos/azul/EnemigoAzul1.png').convert_alpha()
            enemigo_top_2 = pygame.image.load('assets/enemigos/azul/EnemigoAzul2.png').convert_alpha()
            enemigo_top_3 = pygame.image.load('assets/enemigos/azul/EnemigoAzul3.png').convert_alpha()
            enemigo_top_4 = pygame.image.load('assets/enemigos/azul/EnemigoAzul4.png').convert_alpha()
            enemigo_top_5 = pygame.image.load('assets/enemigos/azul/EnemigoAzul5.png').convert_alpha()
            enemigo_top_6 = pygame.image.load('assets/enemigos/azul/EnemigoAzul6.png').convert_alpha()
            enemigo_top_7 = pygame.image.load('assets/enemigos/azul/EnemigoAzul7.png').convert_alpha()
            enemigo_top_8 = pygame.image.load('assets/enemigos/azul/EnemigoAzul8.png').convert_alpha()
            self.frames = [enemigo_top_1, enemigo_top_2, enemigo_top_3, enemigo_top_4, enemigo_top_5, enemigo_top_6, enemigo_top_7, enemigo_top_8]
            x_pos = randint(-200,0)
            y_pos = random.choice([90, 160, 230]) #random entre los tres carriles de arriba
            
        elif type == 'bot':
            enemigo_bot_1 = pygame.image.load('assets/enemigos/rojo/EnemigoRojo1.png').convert_alpha()
            enemigo_bot_2 = pygame.image.load('assets/enemigos/rojo/EnemigoRojo2.png').convert_alpha()
            enemigo_bot_3 = pygame.image.load('assets/enemigos/rojo/EnemigoRojo3.png').convert_alpha()
            enemigo_bot_4 = pygame.image.load('assets/enemigos/rojo/EnemigoRojo4.png').convert_alpha()
            enemigo_bot_5 = pygame.image.load('assets/enemigos/rojo/EnemigoRojo5.png').convert_alpha()
            enemigo_bot_6 = pygame.image.load('assets/enemigos/rojo/EnemigoRojo6.png').convert_alpha()
            enemigo_bot_7 = pygame.image.load('assets/enemigos/rojo/EnemigoRojo7.png').convert_alpha()
            enemigo_bot_8 = pygame.image.load('assets/enemigos/rojo/EnemigoRojo8.png').convert_alpha()
            self.frames = [enemigo_bot_1, enemigo_bot_2, enemigo_bot_3, enemigo_bot_4, enemigo_bot_5, enemigo_bot_6, enemigo_bot_7, enemigo_bot_8]
            x_pos = randint(900,1100)
            y_pos = random.choice([340, 410, 480]) #random entre los tres carriles de abajo
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (x_pos,y_pos))

    def animation_state(self):
        self.animation_index += 0.1 
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()

class Jugador(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'blue':
            jugador_blue_1 = pygame.image.load('assets/jugadores/azul/blueRobot1.png').convert_alpha()
            jugador_blue_2 = pygame.image.load('assets/jugadores/azul/blueRobot2.png').convert_alpha()
            jugador_blue_3 = pygame.image.load('assets/jugadores/azul/blueRobot3.png').convert_alpha()
            jugador_blue_4 = pygame.image.load('assets/jugadores/azul/blueRobot4.png').convert_alpha()
            jugador_blue_5 = pygame.image.load('assets/jugadores/azul/blueRobot5.png').convert_alpha()
            jugador_blue_6 = pygame.image.load('assets/jugadores/azul/blueRobot6.png').convert_alpha()
            jugador_blue_7 = pygame.image.load('assets/jugadores/azul/blueRobot7.png').convert_alpha()
            jugador_blue_8 = pygame.image.load('assets/jugadores/azul/blueRobot8.png').convert_alpha()
            self.player_walk = [jugador_blue_1, jugador_blue_2, jugador_blue_3, jugador_blue_4, jugador_blue_5, jugador_blue_6, jugador_blue_7, jugador_blue_8]
            

        elif type == 'red':
            jugador_red_1 = pygame.image.load('assets/jugadores/rojo/redRobot1.png').convert_alpha()
            jugador_red_2 = pygame.image.load('assets/jugadores/rojo/redRobot2.png').convert_alpha()
            jugador_red_3 = pygame.image.load('assets/jugadores/rojo/redRobot3.png').convert_alpha()
            jugador_red_4 = pygame.image.load('assets/jugadores/rojo/redRobot4.png').convert_alpha()
            jugador_red_5 = pygame.image.load('assets/jugadores/rojo/redRobot5.png').convert_alpha()
            jugador_red_6 = pygame.image.load('assets/jugadores/rojo/redRobot6.png').convert_alpha()
            jugador_red_7 = pygame.image.load('assets/jugadores/rojo/redRobot7.png').convert_alpha()
            jugador_red_8 = pygame.image.load('assets/jugadores/rojo/redRobot8.png').convert_alpha()
            self.player_walk = [jugador_red_1, jugador_red_2, jugador_red_3, jugador_red_4, jugador_red_5, jugador_red_6, jugador_red_7, jugador_red_8]
        
        self.player_index = 0
        #self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        #self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        #self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print("arriba")
        elif keys[pygame.K_DOWN]:
            print("abajo")

    def animation_state(self):
        self.player_index += 0.1 
        if self.player_index >= len(self.player_walk): self.player_index = 0
        self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.animation_state()
        
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("R0B0 / K1LL")
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/RobotRoc.otf', 32)
#========
game_active = False
start_time = 0
score = 0
#bg_music = pygame.mixer.Sound('audio/music.wav')
#bg_music.play(loops = -1)
#========

#========Groups
player = pygame.sprite.GroupSingle()
player.add(Jugador('blue'))

obstacle_group = pygame.sprite.Group()
groundSurface = pygame.image.load("assets/fondov1.png").convert()
#textSurface = testFont.render('R0B0 / K1LL', False, 'Black')
#text_rectangle = textSurface.get_rect(center = (450, 250))

#========Intro screen

#========

#========Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)
#========

#player1_surface = pygame.image.load('assets/P1.png').convert_alpha()
#player1_surface = pygame.transform.scale2x(player1_surface)
#player1_rectangle = player1_surface.get_rect(midbottom = (20 + 32, 20 + 210))

#player2_surface = pygame.image.load('assets/P2.png').convert_alpha()
#player2_surface = pygame.transform.scale2x(player2_surface)
#player2_rectangle = player2_surface.get_rect(midbottom = (WIDTH - 20 - 32, HEIGHT - 20))

#enemigo_surface = pygame.image.load('assets/enemigo.png').convert_alpha()
#enemigo_surface = pygame.transform.scale2x(enemigo_surface)
#enemigo_rectangle = enemigo_surface.get_rect(center = (900 - 32, 32))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Enemigo(choice(['fly','snail','snail','snail'])))
		
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)

    
	#if game_active:
		#WIN.blit(sky_surface,(0,0))
		WIN.blit(groundSurface,(0,300))
		#score = display_score()
		
		player.draw(WIN)
		player.update()

		obstacle_group.draw(WIN)
		obstacle_group.update()

		#game_active = collision_sprite()
		
	#else:
	#	WIN.fill((94,129,162))
		#WIN.blit(player_stand,player_stand_rect)

		#score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		#score_message_rect = score_message.get_rect(center = (400,330))
		#WIN.blit(game_name,game_name_rect)

		#if score == 0: WIN.blit(game_message,game_message_rect)
		#else: WIN.blit(score_message,score_message_rect)

	pygame.display.update()
	clock.tick(60)