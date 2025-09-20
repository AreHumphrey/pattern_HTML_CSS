
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