import pygame
import os
import random

pygame.init()

TELA_LARGURA, TELA_ALTURA = 1200, 600

m = 35  # 1 meteoro a cada m frames (em média quando adicionar aleatoriedade)
l = 15  # 1 laser a cada l frames

IMAGEM_NAVE = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'xwing.png')), (75, 70))
IMAGEM_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'bg_espaco.jpg')),
                                           (TELA_LARGURA, TELA_ALTURA))
IMAGEM_METEORO = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'meteoro.png')), (70, 45))
IMAGEM_LASER = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'laser.png')), (20, 20))

# iniciando a fonte q vai escrever a pontuação na tela
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Nave:
    imagem = IMAGEM_NAVE

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lasers = []
        self.remover_lasers = []

    def mover_p_cima(self):
        self.y -= 15

    def mover_p_baixo(self):
        self.y += 15

    def mover_p_direita(self):
        self.x += 15

    def mover_p_esquerda(self):
        self.x -= 15

    def desenhar(self, tela):
        imagem = self.imagem
        tela.blit(imagem, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Meteoro:
    imagem = IMAGEM_METEORO

    def __init__(self, x):
        self.x = x
        self.y = random.randrange(0, 600 - self.imagem.get_height() * 2)

    def mover_p_esquerda(self):
        self.x -= 10

    def desenhar(self, tela):
        imagem = self.imagem
        tela.blit(imagem, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

    def colidir(self, objeto):
        objeto_mask = objeto.get_mask()
        meteoro_mask = self.get_mask()
        colidiu = objeto_mask.overlap(meteoro_mask, (self.x - objeto.x, self.y - objeto.y))  # retorna True ou False
        return colidiu


class Laser:
    imagem = IMAGEM_LASER

    def __init__(self, nave):
        self.x = nave.x + nave.imagem.get_width() - 20
        self.y = round(nave.imagem.get_height() / 2 + nave.y - 7)

    def mover(self):
        self.x += 25

    def desenhar(self, tela):
        imagem = self.imagem
        tela.blit(imagem, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


def desenhar_na_tela(tela, bg, nave, meteoros, pontos):
    tela.blit(bg, (0, 0))
    nave.desenhar(tela)
    # desenha cada meteoro na tela
    for meteoro in meteoros:
        meteoro.desenhar(tela)

    for laser in nave.lasers:
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

    # Criando lista de meteoros
    meteoros = []

    # Variáveis para controlar a repetição da tecla
    w_pressionada, s_pressionada, d_pressionada, a_pressionada = False, False, False, False
    repeat_interval = 10  # Intervalo em milissegundos para repetição
    last_key_repeat_time = 0

    cont_met = m  # contador de frames p ajudar na criação de meteoros (1 meteóro a cada 40 iterações ou frames)
    cont_laser = l  # 1 laser a cada 20 iterações ou frames
    cont_vel_meteoro = 0  # p ajudar a controlar e aumentar a velocidade de lançamento de meteoro
    cont_vel_laser = 0  # p ajudar a controlar e aumentar a velocidade de lançamento de meteoro
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
                if evento.key == pygame.K_w:
                    w_pressionada = True
                if evento.key == pygame.K_s:
                    s_pressionada = True
                if evento.key == pygame.K_d:
                    d_pressionada = True
                if evento.key == pygame.K_a:
                    a_pressionada = True
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_w:
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
        aleatorio = random.randint(0, 100)  # Colocar uma chance de criação fora do padrão de meteoro. Atenção: não é
        # 1 em 100
        if cont_met >= m - cont_vel_meteoro or aleatorio == 0:
            cont_met = 0
            meteoros.append(Meteoro(TELA_LARGURA))
        # cada meteoro da lista meteoros se move
        for meteoro in meteoros:
            meteoro.mover_p_esquerda()

        # tira os meteoros da lista se passarem do limite da tela (p esquerda, óbvio)
        remover_meteoros = []
        for meteoro in meteoros:
            if meteoro.x <= -meteoro.imagem.get_width():
                remover_meteoros.append(meteoro)
        for meteoro in remover_meteoros:
            meteoros.remove(meteoro)

        # verificar colisao com laser e ja remover o meteoro e o laser
        remover_meteoros = []
        for meteoro in meteoros:
            for laser in xwing.lasers:
                if meteoro.colidir(laser):
                    pontos += 1
                    remover_meteoros.append(meteoro)
                    xwing.remover_lasers.append(laser)
        for meteoro in remover_meteoros:
            meteoros.remove(meteoro)
        for laser in xwing.remover_lasers:
            xwing.lasers.remove(laser)
        xwing.remover_lasers = []

        # verificar colisao de meteoro com nave
        for meteoro in meteoros:
            if meteoro.colidir(xwing):
                rodando = False

        # criar lasers de tempo em tempo
        if cont_laser >= l - cont_vel_laser:
            cont_laser = 0
            xwing.lasers.append(Laser(xwing))
        # cada laser se move
        for laser in xwing.lasers:
            laser.mover()

        # remove os lasers da lista se passarem do limite da tela (p direita, óbvio)
        for laser in xwing.lasers:
            if laser.x >= TELA_LARGURA:
                xwing.remover_lasers.append(laser)
        for laser in xwing.remover_lasers:
            xwing.lasers.remove(laser)
        xwing.remover_lasers = []

        # delimitar a posição da nave
        if xwing.x >= TELA_LARGURA - xwing.imagem.get_width():
            xwing.x = TELA_LARGURA - xwing.imagem.get_width()
        if xwing.x <= 0:
            xwing.x = 0
        if xwing.y >= TELA_ALTURA - xwing.imagem.get_height() / 2:
            xwing.y = TELA_ALTURA - xwing.imagem.get_height() / 2
        if xwing.y <= -xwing.imagem.get_height() / 2:
            xwing.y = -xwing.imagem.get_height() / 2

        # verifica se algum meteoro passou até o final e já encerra o jogo se passou
        for meteoro in meteoros:
            if meteoro.x == 0:
                rodando = False


        cont_met += 1
        cont_laser += 1

        # ir aumentando a velocidade de lançamento de meteoro e laser (exponencialmente) até um limite
        if cont_vel_meteoro <= 15:  # estabelecendo um limite p velocidade de lançamento de meteóros
            cont_vel_meteoro += 0.002  # lembrar que isso é exponencial
        if cont_vel_laser <= 6:  # limite p velocidade de lançamento de lasers também
            cont_vel_laser += 0.002  # isso também é exponencial


        desenhar_na_tela(tela, IMAGEM_BACKGROUND, xwing, meteoros, pontos)
        pygame.time.Clock().tick(30)  # 30 fps



if __name__ == '__main__':
    main()
