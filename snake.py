import pygame
from random import randint
from pygame.locals import *
pygame.init()
tela = pygame.display.set_mode((600,600))

def lugar_aleatorio():
    x = randint(0, 590)
    y = randint(0, 590)
    a = x // 10 * 10
    b = y // 10 * 10
    return (a, b)
def comer_comida(celula1, celula2):
    return (celula1[0] == celula2[0] and celula1[1] == celula2[1])


CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

cobra = [(200, 200), (210, 200), (220, 200)]
cobra_cor = pygame.Surface((10, 10))
cobra_cor.fill((255, 255, 255))

comida_pos = lugar_aleatorio()
comida = pygame.Surface((10, 10))
comida.fill((255, 0, 0))

minha_direcao = ESQUERDA

tempo = pygame.time.Clock()

while True:
    tempo.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                minha_direcao = CIMA
            if event.key == K_DOWN:
                minha_direcao = BAIXO
            if event.key == K_RIGHT:
                minha_direcao = DIREITA
            if event.key == K_LEFT:
                minha_direcao = ESQUERDA

    if comer_comida(cobra[0], comida_pos):
        comida_pos = lugar_aleatorio()
        cobra.append((0, 0))

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i -1][0], cobra[i-1][1])

    if minha_direcao == CIMA:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if minha_direcao == BAIXO:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if minha_direcao == DIREITA:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if minha_direcao == ESQUERDA:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i -1][0], cobra[i-1][1])

    tela.fill((0, 0, 0))
    tela.blit(comida, comida_pos)
    for pos in cobra:
        tela.blit(cobra_cor, pos)

    pygame.display.update()