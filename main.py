import pygame
from constants import *
from player import Player
from world import World

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(50,SCREEN_HEIGHT-101,20,50,5,"red")
    clock = pygame.time.Clock()
    FPS = 30
    world = World(WORLD_DATA)

    while(True):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        draw_grid(screen)
        world.draw(screen)
        # for platform in platforms:
        #     platform.draw(screen)

        player.update(world.tile_list)
        player.draw(screen)
        pygame.display.flip()

def draw_grid(screen):
    for line in range(0,int(SCREEN_HEIGHT/TILE_SIZE)):
        pygame.draw.line(screen,(255,255,255),(0,line*TILE_SIZE),(SCREEN_WIDTH,line*TILE_SIZE))
    for line in range(0,int(SCREEN_WIDTH/TILE_SIZE)):
        pygame.draw.line(screen,(255,255,255),(line*TILE_SIZE,0),(line*TILE_SIZE,SCREEN_HEIGHT))


if __name__ == "__main__":
    main()

