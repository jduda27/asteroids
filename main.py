import pygame
from constants import *

def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))


if __name__ == "__main__":
    main()
