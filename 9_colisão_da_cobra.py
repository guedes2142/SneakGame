# importatndo bibliotecas
import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

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
sneakcolid = pygame.mixer.Sound('mixkit-ominous-drums-227.wav')
sneakcolid  .set_volume(0.5)
score = pygame.mixer.Sound('wwoods-snes_cpu1.wav')

# -----------------------------

x_sneak = int(largura/2)
y_sneak = int(altura/2)
clock = pygame.time.Clock()
velocidade = 1
x_controle = velocidade
y_controle = 0

x_apple = randint(70, 120)
y_apple = randint(50, 400)

fonte = pygame.font.SysFont('lettergothicstdopentype', 20, False, False)

lista_sneak = []
tamanha_inicial = 200
pontos = 0
ameOver = False


def aumentaCobra(lista_cobra):

    for XeY in lista_cobra:
        pygame.draw.rect(windows, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def reiniciarJogo():

    global pontos, tamanha_inicial, x_sneak, y_sneak, lista_cabeça, \
        x_apple, y_apple, gameOver

    pontos = 0
    tamanha_inicial = 20
    x_sneak = int(largura/2)
    y_sneak = int(altura/2)
    lista_sneak = []
    lista_cabeça = []
    x_apple = randint(70, 120)
    y_apple = randint(50, 400)
    gameOver = False


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

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_sneak = x_sneak + x_controle
    y_sneak = y_sneak + y_controle

    sneak = pygame.draw.rect(windows, (0, 255, 0), (x_sneak, y_sneak, 20, 20))

    apple = pygame.draw.circle(windows, (255, 0, 0), (x_apple, y_apple), 10)
    
    wallOne = pygame.draw.rect(windows, (0, 0, 255), (150, 400, 80, 80))
    wallTwo = pygame.draw.rect(windows, (0, 0, 255), (500, 50 , 100, 100))
    
    if sneak.colliderect(wallOne):
        font_2 = pygame.font.SysFont(
            'lettergothicstdopentype', 30, True, False)
        messagem = 'Game Over! precione R para jogar novamente'
        textoFOrmartado = font_2.render(messagem, True, (255, 0, 0))
        rest_texto = textoFOrmartado.get_rect()
        sneakcolid.play()
        gameOver = True
        while gameOver:
            windows.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciarJogo()
                    
            rest_texto.center = (largura//2, altura//2)
            windows.blit(textoFOrmartado, (rest_texto))
            pygame.display.update()

    if sneak.colliderect(apple):

        y_apple = randint(10, 600)
        x_apple = randint(10, 600)

        pontos = pontos + 1
        if pontos == 30:
            score.play()
        if pontos == 60:
            score.play()
            score.play()
        if pontos == 90:
            score.play()
        colisao.play()

        tamanha_inicial = tamanha_inicial + 2

    lista_cabeça = []
    lista_cabeça.append(x_sneak)
    lista_cabeça.append(y_sneak)
    lista_sneak.append(lista_cabeça)

    if lista_sneak.count(lista_cabeça) > 1:

        sneakcolid.play()
        font_2 = pygame.font.SysFont(
            'lettergothicstdopentype', 30, True, False)
        messagem = 'Game Over! precione R para jogar novamente'
        textoFOrmartado = font_2.render(messagem, True, (255, 0, 0))
        rest_texto = textoFOrmartado.get_rect()

        gameOver = True
        while gameOver:
            windows.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciarJogo()
                      
            rest_texto.center = (largura//2, altura//2)
            windows.blit(textoFOrmartado, (rest_texto))
            pygame.display.update()

    if x_sneak > largura:
        x_sneak = 0
    if x_sneak < 0:
        x_sneak = largura
    if y_sneak < 0:
        y_sneak = - altura
    if y_sneak > altura:
        y_sneak = 0

    if len(lista_sneak) > tamanha_inicial:
        del lista_sneak[0]
    aumentaCobra(lista_sneak)

 # -----------------------------
    windows.blit(texto_Formatado, (10, 10))

    pygame.display.update()
