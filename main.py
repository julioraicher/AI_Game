import pygame
import os
import random


# ir testando esses valores
TELA_LARGURA = 800
TELA_ALTURA = 500

IMAGEM_XWING = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'xwing.png')), (50, 50))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'bg.jpg')))
IMAGEM_METEORO = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'meteoro.png')), (25, 25))
IMAGEM_LASER = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'laser.png')), (10, 10))




# testando o tamanho das imagens desenhando na tela (desenhar())
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
tela.blit(IMAGEM_BACKGROUND, (0, 0))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            quit()
