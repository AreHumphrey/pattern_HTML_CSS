import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 15
BALL_SIZE = 20
PLATFORM_SPEED = 8
BALL_SPEED = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
#

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("😜😜😜😜")

platform = pygame.Rect(WIDTH // 2 - PLATFORM_WIDTH // 2,\
                       HEIGHT - 30,
                       PLATFORM_WIDTH, PLATFORM_HEIGHT)

ball = pygame.Rect(random.randint(0, WIDTH - BALL_SIZE),\
                   0, BALL_SIZE, BALL_SIZE)

ball_speed_x = random.choice([-BALL_SPEED, BALL_SPEED])
ball_speed_y = BALL_SPEED

score = 0

font = pygame.font.SysFont("comicsans", 30)

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and platform.left > 0:
        platform.x -= PLATFORM_SPEED
    # K_LEFT - K_w
    # K_RIGHT - K_d
    if keys[pygame.K_RIGHT] and platform.right < WIDTH:
        platform.x += PLATFORM_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0:
        ball_speed_x = -ball_speed_x

    if ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x

    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    if ball.top > HEIGHT:
        score -= 1

        ball.x = random.randint(0, WIDTH - BALL_SIZE)
        ball.y = 0

        ball_speed_y = BALL_SPEED
        ball_speed_x = random.choice([-BALL_SPEED, BALL_SPEED])

    if ball.colliderect(platform) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y
        score += 1
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, platform)
    pygame.draw.circle(screen, WHITE, ball.center,BALL_SIZE // 2)

    score_text = font.render("Счёт: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()