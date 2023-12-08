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

    def desenhar(self, tela):
        imagem = IMAGEM_NAVE
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem.get_rect(topleft=(self.x, self.y))
        tela.blit(imagem, retangulo.topleft)
        pygame.display.update()

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)



def main():
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    xwing = Nave(0, 0)
    rodando = True
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                # Verifica se a tecla pressionada é a tecla desejada
                if evento.key == pygame.K_w:  # ir p cima
                    xwing.mover_p_cima()
                if evento.key == pygame.K_s:
                    xwing.mover_p_baixo()
                if evento.key == pygame.K_d:
                    xwing.mover_p_direita()
                if evento.key == pygame.K_a:
                    xwing.mover_p_esquerda()
        xwing.mover()
        xwing.desenhar(tela)

main()
