import pygame
import random
pygame.init()

# Configuração da tela
largura, altura = 500, 400
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Meu Primeiro Game")

# Definição das cores
branco = (255, 255, 255)
vermelho = (200, 0, 0)
azul = (0, 0, 255)

# Posição inicial do quadrado
x, y = 200, 150
velocidade = 5

# Posição inicial do triângulo
tri_x = random.randint(50, largura - 50)
tri_y = random.randint(50, altura - 50)

# Variável de pontuação
pontuacao = 0

# Loop principal do jogo
rodando = True
while rodando:
    pygame.time.delay(50)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Captura das teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: x -= velocidade
    if teclas[pygame.K_RIGHT]: x += velocidade
    if teclas[pygame.K_UP]: y -= velocidade
    if teclas[pygame.K_DOWN]: y += velocidade

    # Verifica colisão com o triângulo
    if abs(x - tri_x) < 40 and abs(y - tri_y) < 40:
        pontuacao += 1
        tri_x = random.randint(50, largura - 50)
        tri_y = random.randint(50, altura - 50)

    # Atualização da tela
    tela.fill(branco)

    # Desenhar o quadrado
    pygame.draw.rect(tela, vermelho, (x, y, 50, 50))

    # Desenhar o triângulo azul
    pontos = [(tri_x, tri_y), (tri_x - 20, tri_y + 40), (tri_x + 20, tri_y + 40)]
    pygame.draw.polygon(tela, azul, pontos)

    # Exibir pontuação
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(f'Pontuação: {pontuacao}', True, (0, 0, 0))
    tela.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()
