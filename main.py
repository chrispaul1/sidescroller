import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(50,SCREEN_HEIGHT-30,20,30,3,"red")
    clock = pygame.time.Clock()
    FPS = 60

    while(True):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update()
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
