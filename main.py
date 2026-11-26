import pygame
import sys
from player import Player

pygame.init()

# Screen
width,height = 1000,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ECLIPSE")

clock = pygame.time.Clock()

BACKGROUND = (18, 18, 18)
GROUND_COLOR = (55, 53, 58)
PLATFORM_COLOR = (75,72,80)

platforms = [
    pygame.Rect(0,540,1000,60),
    pygame.Rect(200,440,180,20),
    pygame.Rect(480,360,180,20),
    pygame.Rect(750,450,150,20)
]

player = Player((100,480))

running = True
while running:
    dt = min(clock.tick(60)/ 1000, 0.033)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                player.jump()

    keys = pygame.key.get_pressed()

    player.collision(platforms)
    player.update(dt)

    screen.fill(BACKGROUND)

    for platform in platforms:
        pygame.draw.rect(screen,GROUND_COLOR if platform.height > 30 else PLATFORM_COLOR, platform)

    player.move(keys,dt)
    player.draw(screen)

    pygame.display.flip()

    # player.input()
    player.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()