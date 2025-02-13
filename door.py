import pygame
from constants import *
door_group = pygame.sprite.Group()
class Door(pygame.sprite.Sprite):
    containers = (door_group,)
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        for c in self.__class__.containers:
            c.add(self)
        door_img  = pygame.image.load('images/door_PNG.png')
        self.image = pygame.transform.scale(door_img,(TILE_SIZE,TILE_SIZE*2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y