import pygame
from constants import *
lava_group = pygame.sprite.Group()
class Lava(pygame.sprite.Sprite):
    containers = (lava_group,) 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        for c in self.__class__.containers:
            c.add(self)
        lava_img = pygame.image.load("images/Lava_PNG.png")
        self.image = pygame.transform.scale(lava_img,(TILE_SIZE,TILE_SIZE//2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)
