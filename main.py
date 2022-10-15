from tkinter import Toplevel
import pygame
from sys import *

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hola como estas")
clock = pygame.time.Clock()
testFont = pygame.font.Font('fonts/Pixeltype.ttf',50)

groundSurface = pygame.image.load("assets/fondov1.png").convert()
textSurface = testFont.render('auxilio' , False, 'Black')

player1_surface = pygame.image.load('assets/P1.png').convert_alpha()
player1_surface = pygame.transform.scale2x(player1_surface)
player1_rectangle = player1_surface.get_rect(midbottom = (20 + 32, 20 + 210))

player2_surface = pygame.image.load('assets/P2.png').convert_alpha()
player2_surface = pygame.transform.scale2x(player2_surface)
player2_rectangle = player2_surface.get_rect(midbottom = (WIDTH - 20 - 32, HEIGHT - 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    WIN.blit(groundSurface, (0,0) )
    WIN.blit(textSurface, (300, 50))
    WIN.blit(player1_surface, player1_rectangle)
    WIN.blit(player2_surface, player2_rectangle)

    pygame.display.update()
    clock.tick(60)