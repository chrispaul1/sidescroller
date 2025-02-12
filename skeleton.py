import pygame
from constants import *

skelly_group = pygame.sprite.Group()
class Skeleton(pygame.sprite.Sprite):
    containers = (skelly_group,)
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        for c in self.__class__.containers:
            c.add(self)
        skelly_img = pygame.image.load("images/Skeleton_PNG.png")
        self.image = pygame.transform.scale(skelly_img,(TILE_SIZE*.5,TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 2
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
        


