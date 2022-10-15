from tkinter import Toplevel
import pygame
from sys import *

from tkinter import Toplevel
import pygame
from sys import *

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hola como estas")
clock = pygame.time.Clock()
testFont = pygame.font.Font('fonts/Pixeltype.ttf',50)

groundSurface = pygame.image.load("assets/fondo.png").convert()
textSurface = testFont.render('auxilio' , False, 'Black')

player_surface = pygame.image.load('assets/jugador.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, HEIGHT-125))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    
    WIN.blit(groundSurface, (0,0) )
    WIN.blit(textSurface, (300, 50))
    WIN.blit(player_surface, player_rectangle)

    pygame.display.update()
    clock.tick(60)