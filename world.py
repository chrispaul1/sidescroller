import pygame
from constants import *
from skeleton import Skeleton,skelly_group
from lava import Lava,lava_group

class World():
    def __init__(self,data):
        self.tile_list=[]
        self.skeleton_list=[]
        dirt_img = pygame.image.load('images/Dirt_PNG.png')
        grass_img = pygame.image.load('images/Grass_PNG.png')
        coin_img = pygame.image.load("images/Coin_PNG.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*TILE_SIZE
                    img_rect.y = row_count*TILE_SIZE
                    tile=(img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 2:
                    img = pygame.transform.scale(grass_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*TILE_SIZE
                    img_rect.y = row_count*TILE_SIZE
                    tile=(img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 3:
                    lava = Lava(col_count*TILE_SIZE,row_count*TILE_SIZE+TILE_SIZE//2)
                elif tile == 4:
                    skeleton = Skeleton(col_count*TILE_SIZE+TILE_SIZE//4,row_count*TILE_SIZE)

                col_count += 1
            row_count += 1

    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])