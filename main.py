import pygame
import os
import random

# ir testando esses valores
TELA_LARGURA = 1200
TELA_ALTURA = 600

IMAGEM_NAVE = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'xwing.png')), (75, 70))
IMAGEM_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'bg_espaco.jpg')), (1200, 600))
IMAGEM_METEORO = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'meteoro.png')), (60, 40))
IMAGEM_LASER = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'laser.png')), (15, 15))


class Nave:
    def __int__(self, x, y):
        self.x = x
        self.y = y
        self.vel_y = 0
        self.vel_x = 0
        self.imagem = IMAGEM_NAVE

    def mover_p_cima(self):
        self.vel_y = -10

    def mover_p_baixo(self):
        self.vel_y = 10

    def mover_p_direita(self):
        self.vel_x = 15

    def mover_p_esquerda(self):  # fazer uma velocidade menor do que a da direita
        self.vel_x = -7

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y