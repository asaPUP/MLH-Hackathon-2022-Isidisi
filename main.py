from tkinter import Toplevel
import pygame
from numpy.random import choice
from sys import *
from random import *
import numpy as np

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,type,dalt):
        super().__init__()

        if type == 'top':
            if dalt == False:
                enemigo_top_1 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo1.png').convert_alpha())
                enemigo_top_2 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo2.png').convert_alpha())
                enemigo_top_3 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo3.png').convert_alpha())
                enemigo_top_4 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo4.png').convert_alpha())
                enemigo_top_5 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo5.png').convert_alpha())
                enemigo_top_6 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo6.png').convert_alpha())
                enemigo_top_7 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo7.png').convert_alpha())
                enemigo_top_8 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo8.png').convert_alpha())
            elif dalt == False:
                enemigo_top_1 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo1.png').convert_alpha())
                enemigo_top_2 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo2.png').convert_alpha())
                enemigo_top_3 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo3.png').convert_alpha())
                enemigo_top_4 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo4.png').convert_alpha())
                enemigo_top_5 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo5.png').convert_alpha())
                enemigo_top_6 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo6.png').convert_alpha())
                enemigo_top_7 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo7.png').convert_alpha())
                enemigo_top_8 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/rojo/EnenemigoRojo8.png').convert_alpha())
            
            self.frames = [enemigo_top_1, enemigo_top_2, enemigo_top_3, enemigo_top_4, enemigo_top_5, enemigo_top_6, enemigo_top_7, enemigo_top_8]
            x_pos = randint(900,1100)
            y_pos = choice([90, 160, 230]) #random entre los tres carriles de arriba
            
        elif type == 'bot':
            enemigo_bot_1 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/azul/EnemigoAzul1.png').convert_alpha())
            enemigo_bot_2 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/azul/EnemigoAzul2.png').convert_alpha())
            enemigo_bot_3 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/azul/EnemigoAzul3.png').convert_alpha())
            enemigo_bot_4 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/azul/EnemigoAzul4.png').convert_alpha())
            enemigo_bot_5 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/azul/EnemigoAzul5.png').convert_alpha())
            enemigo_bot_6 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/azul/EnemigoAzul6.png').convert_alpha())
            enemigo_bot_7 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/azul/EnemigoAzul7.png').convert_alpha())
            enemigo_bot_8 = pygame.transform.scale2x(pygame.image.load('assets/enemigos/azul/EnemigoAzul8.png').convert_alpha())
            
            self.frames = [enemigo_bot_1, enemigo_bot_2, enemigo_bot_3, enemigo_bot_4, enemigo_bot_5, enemigo_bot_6, enemigo_bot_7, enemigo_bot_8]
            x_pos = randint(-200,0)
            y_pos = choice([340, 410, 480]) #random entre los tres carriles de abajo
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (x_pos,y_pos))

    def animation_state(self):
        self.animation_index += 0.5
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        if self.rect.y <= 250:
            self.rect.x -= 5
        else:
            self.rect.x += 5
        self.destroy()

    def destroy(self):
        if self.rect.y <= 250:
            if self.rect.x >= 1000:
                self.kill()
        else:
            if self.rect.x <= -100:
                self.kill()

class Jugador(pygame.sprite.Sprite):
    def __init__(self,type,dalt):
        super().__init__()
        
        if type == 'blue':
            jugador_blue_1 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/azul/blueRobot1.png').convert_alpha())
            jugador_blue_2 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/azul/blueRobot2.png').convert_alpha())
            jugador_blue_3 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/azul/blueRobot3.png').convert_alpha())
            jugador_blue_4 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/azul/blueRobot4.png').convert_alpha())
            jugador_blue_5 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/azul/blueRobot5.png').convert_alpha())
            jugador_blue_6 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/azul/blueRobot6.png').convert_alpha())
            jugador_blue_7 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/azul/blueRobot7.png').convert_alpha())
            jugador_blue_8 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/azul/blueRobot8.png').convert_alpha())
            
            self.jugador_walk = [jugador_blue_1, jugador_blue_2, jugador_blue_3, jugador_blue_4, jugador_blue_5, jugador_blue_6, jugador_blue_7, jugador_blue_8]
            x_pos = 20 + 32
            y_pos = 160

        elif type == 'red':
            if dalt == False:
                jugador_red_1 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/rojo/redRobot1.png').convert_alpha())
                jugador_red_2 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/rojo/redRobot2.png').convert_alpha())
                jugador_red_3 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/rojo/redRobot3.png').convert_alpha())
                jugador_red_4 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/rojo/redRobot4.png').convert_alpha())
                jugador_red_5 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/rojo/redRobot5.png').convert_alpha())
                jugador_red_6 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/rojo/redRobot6.png').convert_alpha())
                jugador_red_7 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/rojo/redRobot7.png').convert_alpha())
                jugador_red_8 = pygame.transform.scale2x(pygame.image.load('assets/jugadores/rojo/redRobot8.png').convert_alpha())
            elif dalt == True:
                jugador_red_1 = pygame.transform.scale2x(pygame.image.load('assets/redRobotD/redRobotD1.png').convert_alpha())
                jugador_red_2 = pygame.transform.scale2x(pygame.image.load('assets/redRobotD/redRobotD2.png').convert_alpha())
                jugador_red_3 = pygame.transform.scale2x(pygame.image.load('assets/redRobotD/redRobotD3.png').convert_alpha())
                jugador_red_4 = pygame.transform.scale2x(pygame.image.load('assets/redRobotD/redRobotD4.png').convert_alpha())
                jugador_red_5 = pygame.transform.scale2x(pygame.image.load('assets/redRobotD/redRobotD5.png').convert_alpha())
                jugador_red_6 = pygame.transform.scale2x(pygame.image.load('assets/redRobotD/redRobotD6.png').convert_alpha())
                jugador_red_7 = pygame.transform.scale2x(pygame.image.load('assets/redRobotD/redRobotD7.png').convert_alpha())
                jugador_red_8 = pygame.transform.scale2x(pygame.image.load('assets/redRobotD/redRobotD8.png').convert_alpha()) 

            self.jugador_walk = [jugador_red_1, jugador_red_2, jugador_red_3, jugador_red_4, jugador_red_5, jugador_red_6, jugador_red_7, jugador_red_8]
            x_pos = WIDTH - 20 - 32
            y_pos = 410

        self.jugador_index = 0
        self.image = self.jugador_walk[self.jugador_index]
        self.rect = self.image.get_rect(midbottom = (x_pos, y_pos))

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP]):
            print("arriba")
        elif (keys[pygame.K_DOWN]):
            print("abajo")

    def animation_state(self):
        self.jugador_index += 0.5
        if self.jugador_index >= len(self.jugador_walk): self.jugador_index = 0
        self.image = self.jugador_walk[int(self.jugador_index)]

    def update(self):
        self.player_input()
        self.animation_state()
        
pygame.init()

dalt = False

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("R0B0 / K1LL")
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/RobotRoc.otf', 32)

game_active = False
start_time = 0
score = 0

#========Groups
blue_player = pygame.sprite.GroupSingle()
blue_player.add(Jugador('blue'))

red_player = pygame.sprite.GroupSingle()
red_player.add(Jugador('red'))

obstacle_group = pygame.sprite.Group()

if dalt == False:
    fondo_surface = pygame.image.load("assets/marcos/FondoGeneal.png").convert()
    marcos_surface = pygame.image.load("assets/marcos/FondoMarco.png").convert_alpha()
else:
    fondo_surface = pygame.image.load("assets/marcos/FondosD.png").convert()
    marcos_surface = pygame.image.load("assets/marcos/FondoMarco.png").convert_alpha()

textSurface = test_font.render('R0B0 / K1LL', False, 'White')
text_rectangle = textSurface.get_rect(center = (450, 250))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    obstacle_group.add(Enemigo('top'))
    obstacle_group.add(Enemigo('bot'))
        
    WIN.blit(fondo_surface,(0,0))
    WIN.blit(textSurface, text_rectangle)
    
    blue_player.draw(WIN)
    blue_player.update()

    red_player.draw(WIN)
    red_player.update()

    obstacle_group.draw(WIN)
    obstacle_group.update()

    WIN.blit(marcos_surface,(0,0))
    WIN.blit(textSurface, text_rectangle)

    pygame.display.update()
    clock.tick(60)