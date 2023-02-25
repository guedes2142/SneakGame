# importatndo bibliotecas
import pygame
from pygame.locals import *
from sys import exit
from random import randint
# ----------------------------------------------------------------#

pygame.init()

largura = 1180
altura = 620
windows = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu jogo')

# -----------------------------

pygame.mixer.music.set_volume(0.5)
musicafundo = pygame.mixer.music.load('Adventure.mp3')
pygame.mixer.music.play(-1)
colisao = pygame.mixer.Sound('lm_coin.wav')
colisao.set_volume(0.2)


# -----------------------------


x = int(largura/2)
y = int(altura/2)
clock = pygame.time.Clock()


x_green = randint(70, 120)
x_yellow = randint(70, 120)

y_green = randint(70, 120)
y_yellow = randint(50, 400)

fonte = pygame.font.SysFont('lettergothicstdopentype', 20, False, False)

pontos = 0

while True:
    clock.tick(240)
    windows.fill((0, 0, 0))

    # -----------------------------
    messagem = f'Pontuação: {pontos}'
    texto_Formatado = fonte.render(messagem, True, (255, 0, 0))
    # -----------------------------

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 2
    if pygame.key.get_pressed()[K_d]:
        x = x + 2
    if pygame.key.get_pressed()[K_w]:
        y = y - 2
    if pygame.key.get_pressed()[K_s]:
        y = y + 2

    ret_green = pygame.draw.rect(windows, (0, 255, 0), (x, y, 40, 40))
    ret_yellow = pygame.draw.rect(
        windows, (255, 255, 0), (y_yellow, y_yellow, 40, 40))

    if ret_green.colliderect(ret_yellow):
        x_yellow = randint(250, 550)
        y_yellow = randint(250, 550)
# -----------------------------
        colisao.play()
 # -----------------------------
        pontos = pontos + 1
    windows.blit(texto_Formatado, (10, 10))

    pygame.display.update()
