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


x_sneak = int(largura/2)

y_sneak = int(altura/2)

clock = pygame.time.Clock()


x_sneak = randint(70, 120)

y_sneak = randint(70, 120)

velocidade = 1

x_controle = velocidade
y_controle = 0


x_apple = randint(70, 120)

y_apple = randint(50, 400)


fonte = pygame.font.SysFont('lettergothicstdopentype', 20, False, False)


lista_sneak = []

tamanha_inicial = 5

pontos = 0


def aumentaCobra(lista_cobra):

    for XeY in lista_cobra:

        pygame.draw.rect(windows, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


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

    apple = pygame.draw.rect(

        windows, (255, 0, 0), (x_apple, y_apple, 20, 20))

    if sneak.colliderect(apple):

        y_apple = randint(10, 600)

        x_apple = randint(10, 600)

        pontos = pontos + 1
        colisao.play()

        tamanha_inicial = tamanha_inicial + 1

    lista_cabeça = []

    lista_cabeça.append(x_sneak)

    lista_cabeça.append(y_sneak)

    lista_sneak.append(lista_cabeça)

    if len(lista_sneak) > tamanha_inicial:

        del lista_sneak[0]

    aumentaCobra(lista_sneak)

 # -----------------------------

    windows.blit(texto_Formatado, (10, 10))

    pygame.display.update()
