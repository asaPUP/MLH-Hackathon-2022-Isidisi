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
            enemigo_top_1 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_top_2 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_top_3 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_top_4 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_top_5 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_top_6 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_top_7 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_top_8 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            self.frames = [enemigo_top_1, enemigo_top_2, enemigo_top_3, enemigo_top_4, enemigo_top_5, enemigo_top_6, enemigo_top_7, enemigo_top_8]
            x_pos = randint(-200,0)
            y_pos = random.choice([90, 160, 230]) #random entre los tres carriles de arriba
            
        elif type == 'bot':
            enemigo_bot_1 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_bot_2 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_bot_3 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_bot_4 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_bot_5 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_bot_6 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_bot_7 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            enemigo_bot_8 = pygame.image.load('graphics/fly/enemigo.png').convert_alpha()
            self.frames = [enemigo_bot_1, enemigo_bot_2, enemigo_bot_3, enemigo_bot_4, enemigo_bot_5, enemigo_bot_6, enemigo_bot_7, enemigo_bot_8]
            x_pos = randint(900,1100)
            y_pos = random.choice([340, 410, 480]) #random entre los tres carriles de abajo
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (x_pos,y_pos))

class Jugador(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'blue':
            jugador_blue_1 = pygame.image.load('assets/blueRobot/blueRobot1.png').convert_alpha()
            jugador_blue_2 = pygame.image.load('assets/blueRobot/blueRobot2.png').convert_alpha()
            jugador_blue_3 = pygame.image.load('assets/blueRobot/blueRobot3.png').convert_alpha()
            jugador_blue_4 = pygame.image.load('assets/blueRobot/blueRobot4.png').convert_alpha()
            jugador_blue_5 = pygame.image.load('assets/blueRobot/blueRobot5.png').convert_alpha()
            jugador_blue_6 = pygame.image.load('assets/blueRobot/blueRobot6.png').convert_alpha()
            jugador_blue_7 = pygame.image.load('assets/blueRobot/blueRobot7.png').convert_alpha()
            jugador_blue_8 = pygame.image.load('assets/blueRobot/blueRobot8.png').convert_alpha()
            self.frames = [jugador_blue_1, jugador_blue_2, jugador_blue_3, jugador_blue_4, jugador_blue_5, jugador_blue_6, jugador_blue_7, jugador_blue_8]
            x_pos = randint(-200,0)
            y_pos = random.choice([90, 160, 230]) #random entre los tres carriles de arriba
            
        elif type == 'red':
            jugador_red_1 = pygame.image.load('assets/redRobot/redRobot1.png').convert_alpha()
            jugador_red_2 = pygame.image.load('assets/redRobot/redRobot2.png').convert_alpha()
            jugador_red_3 = pygame.image.load('assets/redRobot/redRobot3.png').convert_alpha()
            jugador_red_4 = pygame.image.load('assets/redRobot/redRobot4.png').convert_alpha()
            jugador_red_5 = pygame.image.load('assets/redRobot/redRobot5.png').convert_alpha()
            jugador_red_6 = pygame.image.load('assets/redRobot/redRobot6.png').convert_alpha()
            jugador_red_7 = pygame.image.load('assets/redRobot/redRobot7.png').convert_alpha()
            jugador_red_8 = pygame.image.load('assets/redRobot/redRobot8.png').convert_alpha()
            self.frames = [jugador_red_1, jugador_red_2, jugador_red_3, jugador_red_4, jugador_red_5, jugador_red_6, jugador_red_7, jugador_red_8]
            x_pos = randint(-200,0)
            y_pos = random.choice([90, 160, 230]) #random entre los tres carriles de arriba
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (x_pos,y_pos))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def animation_state(self):
        self.animation_index += 0.1 
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("R0B0 / K1LL")
clock = pygame.time.Clock()
testFont = pygame.font.Font('fonts/RobotRoc.otf', 32)

groundSurface = pygame.image.load("assets/fondov1.png").convert()
textSurface = testFont.render('R0B0 / K1LL', False, 'Black')
text_rectangle = textSurface.get_rect(center = (450, 250))

player1_surface = pygame.image.load('assets/P1.png').convert_alpha()
player1_surface = pygame.transform.scale2x(player1_surface)
player1_rectangle = player1_surface.get_rect(midbottom = (20 + 32, 20 + 210))

player2_surface = pygame.image.load('assets/P2.png').convert_alpha()
player2_surface = pygame.transform.scale2x(player2_surface)
player2_rectangle = player2_surface.get_rect(midbottom = (WIDTH - 20 - 32, HEIGHT - 20))

enemigo_surface = pygame.image.load('assets/enemigo.png').convert_alpha()
enemigo_surface = pygame.transform.scale2x(enemigo_surface)
enemigo_rectangle = enemigo_surface.get_rect(center = (900 - 32, 32))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    WIN.blit(groundSurface, (0,0) )
    WIN.blit(textSurface, text_rectangle)
    WIN.blit(player1_surface, player1_rectangle)
    WIN.blit(player2_surface, player2_rectangle)
    WIN.blit(enemigo_surface, enemigo_rectangle)

    enemigo_rectangle.x -= 5

    pygame.display.update()
    clock.tick(60)