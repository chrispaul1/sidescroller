import pygame
from constants import *
coin_group = pygame.sprite.Group()
class Coin(pygame.sprite.Sprite):
    containers = (coin_group,)
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        for c in self.__class__.containers:
            c.add(self)
        coin_img = pygame.image.load("images/Coin_PNG.png")
        self.image = pygame.transform.scale(coin_img,(TILE_SIZE//2,TILE_SIZE//2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.y += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 5:
            self.move_direction *= -1
            self.move_counter *= -1
