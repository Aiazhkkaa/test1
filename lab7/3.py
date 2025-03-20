import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

RADIUS = 25
x = WIDTH // 2
y = HEIGHT // 2
speed = 20

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x - RADIUS - speed >= 0:
            x -= speed
    if keys[pygame.K_RIGHT]:
        if x + RADIUS + speed <= WIDTH:
            x += speed
    if keys[pygame.K_UP]:
        if y - RADIUS - speed >= 0:
            y -= speed
    if keys[pygame.K_DOWN]:
        if y + RADIUS + speed <= HEIGHT:
            y += speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
