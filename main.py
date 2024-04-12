import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение основных констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Создание игрового окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

# Инициализация переменных для мяча, ракеток и скоростей
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 3 * random.choice((1, -1))
ball_dy = 3 * random.choice((1, -1))

paddle1_y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2
paddle2_y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2
paddle1_dy = 0
paddle2_dy = 0

# Функция отрисовки объектов на экране
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2, 0, 2, SCREEN_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_dy = -5
            elif event.key == pygame.K_s:
                paddle1_dy = 5
            elif event.key == pygame.K_UP:
                paddle2_dy = -5
            elif event.key == pygame.K_DOWN:
                paddle2_dy = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle1_dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle2_dy = 0

    # Обновление координат мяча и ракеток
    ball_x += ball_dx
    ball_y += ball_dy
    paddle1_y += paddle1_dy
    paddle2_y += paddle2_dy

    # Отскок мяча от стен
    if ball_y + BALL_RADIUS >= SCREEN_HEIGHT or ball_y - BALL_RADIUS <= 0:
        ball_dy *= -1
    # Отскок мяча от ракеток
    if ball_x - BALL_RADIUS <= PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
        ball_dx *= -1
    elif ball_x + BALL_RADIUS >= SCREEN_WIDTH - PADDLE_WIDTH and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
        ball_dx *= -1
    # Проверка на выход мяча за границы по горизонтали
    if ball_x + BALL_RADIUS >= SCREEN_WIDTH or ball_x - BALL_RADIUS <= 0:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_dx = 3 * random.choice((1, -1))
        ball_dy = 3 * random.choice((1, -1))

    # Ограничение ракеток в пределах игрового поля
    paddle1_y = max(min(paddle1_y, SCREEN_HEIGHT - PADDLE_HEIGHT), 0)
    paddle2_y = max(min(paddle2_y, SCREEN_HEIGHT - PADDLE_HEIGHT), 0)

    # Отрисовка объектов
    draw_objects()

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

# Завершение игры
pygame.quit()
