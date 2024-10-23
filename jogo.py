import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Definindo constantes
WIDTH, HEIGHT = 800, 600
FPS = 15
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SNAKE_BLOCK = 20

# Configura a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Desenvolvido por Victor Bruno")

# Fonte para o texto
font = pygame.font.SysFont(None, 55)

# Função para mostrar a mensagem inicial
def show_initial_message():
    screen.fill(WHITE)
    message = font.render("Jogo desenvolvido por Victor Bruno", True, (0, 0, 0))
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  # Espera 2 segundos

# Função para desenhar a cobrinha
def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], SNAKE_BLOCK, SNAKE_BLOCK])

# Função para gerar a posição da comida
def random_food_position():
    return (
        random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK),
        random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)
    )

# Loop principal do jogo
def game_loop():
    # Inicializa a cobrinha
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0
    snake_blocks = []
    snake_length = 1

    # Inicializa a comida
    food_x, food_y = random_food_position()

    show_initial_message()  # Exibe a mensagem inicial

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Atualiza a posição da cobrinha
        x += x_change
        y += y_change

        # Verifica se a cobrinha colidiu com as bordas
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            print("Você colidiu com as bordas!")
            pygame.quit()
            sys.exit()

        # Adiciona a nova posição da cobrinha
        snake_blocks.append((x, y))
        if len(snake_blocks) > snake_length:
            del snake_blocks[0]

        # Verifica se a cobrinha colidiu consigo mesma
        if (x, y) in snake_blocks[:-1]:
            print("Você colidiu consigo mesmo!")
            pygame.quit()
            sys.exit()

        # Verifica se a cobrinha comeu a comida
        if x == food_x and y == food_y:
            snake_length += 1
            food_x, food_y = random_food_position()

        # Atualiza a tela
        screen.fill(WHITE)
        draw_snake(snake_blocks)
        pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])  # Desenha a comida
        pygame.display.flip()

        # Controla a taxa de quadros
        clock.tick(FPS)

# Inicia o jogo
game_loop()
