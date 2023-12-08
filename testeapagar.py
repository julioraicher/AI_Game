import pygame

tela = pygame.display.set_mode((500, 500))
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                tela.blit()
                print('deu certo serado p k_a')
