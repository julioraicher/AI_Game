import pygame
import os
import random
from time import sleep

# ir testando esses valores
TELA_LARGURA = 1200
TELA_ALTURA = 600

IMAGEM_XWING = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'xwing.png')), (75, 70))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'bg.jpg'))
IMAGEM_METEORO = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'meteoro.png')), (60, 40))
IMAGEM_LASER = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'laser.png')), (15, 15))


# testando o tamanho das imagens desenhando na tela (desenhar())
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
sleep(1)
tela.blit(IMAGEM_BACKGROUND, (0, 0))
tela.blit(IMAGEM_METEORO, (600, 300))
tela.blit(IMAGEM_XWING, (600, 150))

pygame.display.update()


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            quit()
