import pygame
import os
import random


# ir testando esses valores
TELA_LARGURA = 1200
TELA_ALTURA = 600

IMAGEM_NAVE = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'xwing.png')), (75, 70))
IMAGEM_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'bg_espaco.jpg')), (1200, 600))
IMAGEM_METEORO = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'meteoro.png')), (70, 45))
IMAGEM_LASER = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'laser.png')), (20, 20))

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

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

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Meteoro:
    imagem = IMAGEM_METEORO

    def __init__(self, x):
        self.x = x
        self.y = random.randrange(0, 600 - self.imagem.get_height() * 2)

    def mover_p_esquerda(self):
        self.x -= 10  # (mesma velocidade da nave indo p esquerda)

    def desenhar(self, tela):
        imagem = self.imagem
        tela.blit(imagem, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

    def colidir(self, objeto):
        objeto_mask = objeto.get_mask()
        meteoro_mask = self.get_mask()
        colidiu = objeto_mask.overlap(meteoro_mask, (self.x - objeto.x, self.y - objeto.y))  # True ou False (?)
        return colidiu


class Laser:
    imagem = IMAGEM_LASER

    def __init__(self, nave):
        self.x = nave.x + nave.imagem.get_width() - 20
        self.y = round(nave.imagem.get_height() / 2 + nave.y - 7)

    def mover(self):
        self.x += 25  # testar essa velocidade

    def desenhar(self, tela):
        imagem = self.imagem
        tela.blit(imagem, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


def desenhar_na_tela(tela, bg, nave, meteoros, lasers, pontos):
    tela.blit(bg, (0, 0))
    nave.desenhar(tela)
    # desenha cada meteoro na tela
    for meteoro in meteoros:
        meteoro.desenhar(tela)
    for laser in lasers:
        laser.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

    # atualizando a tela depois de todas as alterações a serem feitas
    pygame.display.update()


def main():
    # iniciando a tela do jogo
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))

    # Iniciando a nave
    xwing = Nave(300, 300)

    # Criando meteoros
    meteoros = []

    # Criando lasers
    lasers = []

    # Variáveis para controlar a repetição da tecla
    w_pressionada, s_pressionada, d_pressionada, a_pressionada = False, False, False, False
    repeat_interval = 10  # Intervalo em milissegundos para repetição
    last_key_repeat_time = 0

    cont_met = 60  # contador de frames p ajudar na criação de meteoros
    cont_laser = 30
    pontos = 0
    rodando = True
    while rodando:
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


        # criar meteoros a cada (intervalo de tempo)
        if cont_met >= 60:
            cont_met = 0
            meteoros.append(Meteoro(1200))
        # cada meteoro da lista meteoros se move
        for meteoro in meteoros:
            meteoro.mover_p_esquerda()
        # tira os meteoros da lista
        remover_meteoros = []
        for meteoro in meteoros:
            if meteoro.x <= meteoro.imagem.get_width() * (-1):
                remover_meteoros.append(meteoro)
        for meteoro in remover_meteoros:
            meteoros.remove(meteoro)
        # verificar colisao com laser e ja remover o meteoro e o laser
        remover_meteoros = []
        remover_lasers = []
        for meteoro in meteoros:
            for laser in lasers:
                if meteoro.colidir(laser):
                    pontos += 1
                    remover_meteoros.append(meteoro)
                    remover_lasers.append(laser)
        for meteoro in remover_meteoros:
            meteoros.remove(meteoro)
        for laser in remover_lasers:
            lasers.remove(laser)
        # verificar colisao com nave
        for meteoro in meteoros:
            if meteoro.colidir(xwing):
                rodando = False

        # criar lasers de tempo em tempo
        if cont_laser >= 30:
            cont_laser = 0
            lasers.append(Laser(xwing))
        # cada laser se move
        for laser in lasers:
            laser.mover()
        # remove os lasers da lista
        remover_lasers = []
        for laser in lasers:
            if laser.x >= 1185:
                remover_lasers.append(laser)
        for laser in remover_lasers:
            lasers.remove(laser)

        # delimitar a posição da nave
        if xwing.x >= 1125:
            xwing.x = 1125
        if xwing.x <= 0:
            xwing.x = 0
        if xwing.y >= 550:
            xwing.y = 550
        if xwing.y <= -25:
            xwing.y = -25


        cont_met += 1
        cont_laser += 1
        pygame.time.Clock().tick(30)  # 30 fps
        desenhar_na_tela(tela, IMAGEM_BACKGROUND, xwing, meteoros, lasers, pontos)


if __name__ == '__main__':
    main()
