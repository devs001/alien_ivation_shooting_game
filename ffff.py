import sys, pygame
from pygame import Color

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(Color(25, 100, 200, 255))
    pygame.display.flip()