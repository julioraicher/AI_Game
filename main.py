import pygame
import os
# import random


# pygame.init()  # precisa disso?


# ir testando esses valores
TELA_LARGURA = 1200
TELA_ALTURA = 600

IMAGEM_NAVE = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'xwing.png')), (75, 70))
IMAGEM_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'bg_espaco.jpg')), (1200, 600))
IMAGEM_METEORO = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'meteoro.png')), (60, 40))
IMAGEM_LASER = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'laser.png')), (15, 15))


class Nave:
    imagem = IMAGEM_NAVE
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_p_cima(self):
        self.y -= 10

    def mover_p_baixo(self):
        self.y += 10

    def mover_p_direita(self):
        self.x += 15

    def mover_p_esquerda(self):  # fazer uma velocidade menor do que a da direita
        self.x -= 10

    def desenhar(self, tela):
        imagem = self.imagem
        # pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem.get_rect(topleft=(self.x, self.y))
        tela.blit(imagem, retangulo.topleft)
        pygame.display.update()

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Meteoro:
    pass


tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
xwing = Nave(300, 300)


# Variáveis para controlar a repetição da tecla
w_pressionada, s_pressionada, d_pressionada, a_pressionada = False, False, False, False
repeat_interval = 10  # Intervalo em milissegundos para repetição
last_key_repeat_time = 0

rodando = True
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            # Verifica se a tecla pressionada é a tecla desejada
            if evento.key == pygame.K_w:  # ir p cima
                w_pressionada = True
            if evento.key == pygame.K_s:
                s_pressionada = True
            if evento.key == pygame.K_d:
                d_pressionada = True
            if evento.key == pygame.K_a:
                a_pressionada = True
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:  # ir p cima
                w_pressionada = False
            if evento.key == pygame.K_s:
                s_pressionada = False
            if evento.key == pygame.K_d:
                d_pressionada = False
            if evento.key == pygame.K_a:
                a_pressionada = False

    if a_pressionada or w_pressionada or s_pressionada or d_pressionada:
        if pygame.time.get_ticks() - last_key_repeat_time > repeat_interval:
            if w_pressionada:
                xwing.mover_p_cima()
            if s_pressionada:
                xwing.mover_p_baixo()
            if d_pressionada:
                xwing.mover_p_direita()
            if a_pressionada:
                xwing.mover_p_esquerda()

            last_key_repeat_time = pygame.time.get_ticks()

    pygame.time.Clock().tick(30)
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    xwing.desenhar(tela)
