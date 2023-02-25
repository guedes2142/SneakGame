# importatndo bibliotecas
import pygame
from pygame.locals import *
from sys import exit
# ----------------------------------------------------------------#

pygame.init()

largura = 1180
altura = 620
windows = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu jogo')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
            
    pygame.draw.rect(windows, (0,255,0), (200, 300, 40, 40))
    pygame.draw.circle(windows, (255,0,0), (300, 260), 40)   
    pygame.draw.line(windows,(255,255,0), (390,0), (390,600), 5)

    pygame.display.update()
