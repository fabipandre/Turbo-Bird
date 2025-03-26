import pygame
import time  # Importando o módulo time

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo 2D")

# Cores
BRANCO = (255, 255, 255)

# Posições iniciais do personagem
pos_x = 100
pos_y = 300

# Clock para controlar a taxa de atualização do jogo
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False  # Sai do loop se fechar a janela

    # Movimentação do personagem
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        pos_x -= 5
    if teclas[pygame.K_RIGHT]:
        pos_x += 5
    if teclas[pygame.K_UP]:
        pos_y -= 5
    if teclas[pygame.K_DOWN]:
        pos_y += 5

    # Preenche a tela com a cor branca
    tela.fill(BRANCO)

    # Desenha o personagem na tela
    pygame.draw.rect(tela, (255, 0, 0), (pos_x, pos_y, 50, 50))

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização do jogo (FPS)
    clock.tick(60)  # 60 FPS

# Encerra o pygame
pygame.quit()

