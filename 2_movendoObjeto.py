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

x = 0
y = 0
clock = pygame.time.Clock()


while True:
    clock.tick(240)
    windows.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(windows, (0, 255, 0), (x, y, 40, 40))

    if y >= altura:
        y= 0
    y = y + 1

    pygame.display.update()
