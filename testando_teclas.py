"""Arquivo feito pelo chat GPT
para ajudar a entender como funciona manter uma tecla apertada
no pygame e no jogo"""

import pygame
import sys

pygame.init()

# Configurações
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Variáveis para controlar a repetição da tecla
key_pressed = False
repeat_interval = 10  # Intervalo em milissegundos para repetição
last_key_repeat_time = 0

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                key_pressed = True
                # Realize a ação inicial aqui

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                key_pressed = False

    # Verifica se a tecla está pressionada e se já é hora de repetir a ação
    if key_pressed and pygame.time.get_ticks() - last_key_repeat_time > repeat_interval:
        # Realize a ação repetida aqui
        print("Tecla pressionada e repetida")
        last_key_repeat_time = pygame.time.get_ticks()

    # Atualiza a tela
    pygame.display.flip()

    # Define a taxa de quadros
    clock.tick(30)
