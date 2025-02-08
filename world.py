import pygame
from constants import *
class World():
    def __init__(self,data):
        self.tile_list=[]
        self.skeleton_list=[]
        dirt_img = pygame.image.load('images/Dirt_PNG.png')
        grass_img = pygame.image.load('images/Grass_PNG.png')
        lava_img = pygame.image.load("images/Lava_PNG.png")
        skeleton_img = pygame.image.load("images/Skeleton_PNG.png")
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
                    img = pygame.transform.scale(lava_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*TILE_SIZE
                    img_rect.y = row_count*TILE_SIZE
                    tile=(img,img_rect)
                    self.tile_list.append(tile)
                elif tile == 4:
                    img = pygame.transform.scale(skeleton_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*TILE_SIZE
                    img_rect.y = row_count*TILE_SIZE
                    tile=(img,img_rect)
                    self.skeleton_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])