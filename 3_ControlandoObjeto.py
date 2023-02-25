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

x = largura/2
y = altura/2
clock = pygame.time.Clock()


while True:
    clock.tick(240)
    windows.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            '''
            #-----------------------------
            if event.key == K_a:
                x = x - 10
            if event.key == K_d:
                x =x + 10
            if event.key == K_w:
                y = y - 10
            if event.key == K_s:
                y = y +  10
            #-----------------------------'''
    if pygame.key.get_pressed()[K_a]:
        x = x - 2
    if pygame.key.get_pressed()[K_d]:
        x = x + 2
    if pygame.key.get_pressed()[K_w]:
        y = y - 2        
    if pygame.key.get_pressed()[K_s]:
        y = y + 2  
                   
    pygame.draw.rect(windows, (0, 255, 0), (x, y, 40, 40))


    pygame.display.update()
