import pygame
from constants import *
from sprite_sheet import get_image

skelly_group = pygame.sprite.Group()
class Skeleton(pygame.sprite.Sprite):
    containers = (skelly_group,)
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        for c in self.__class__.containers:
            c.add(self)
        Black=(0,0,0)
        skelly_sprite = pygame.image.load("images/skeleton-walk.png").convert_alpha()
        self.walk_images_right = []
        self.walk_images_left = []
        self.walk_counter = 0
        self.walk_cooldown = 5
        self.walk_index=0

        for i in range(0,4):
            image_right = get_image(skelly_sprite,i,1,48,48,Black)
            image_left = pygame.transform.flip(image_right,True,False)
            image_left.set_colorkey(Black)
            self.walk_images_right.append(image_right)
            self.walk_images_left.append(image_left)

        skelly_img = pygame.image.load("images/Skeleton_PNG.png")
        self.image = self.walk_images_right[0]
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y+8
        self.move_direction = 2
        self.move_counter = 0
        self.mask = pygame.mask.from_surface(self.image)
    

    def update(self,screen):
        self.rect.x += self.move_direction
        self.move_counter += 1
        self.walk_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
        
        if self.walk_counter > self.walk_cooldown:
            self.walk_counter = 0
            self.walk_index += 1
            if self.walk_index >= len(self.walk_images_right):
                self.walk_index = 0
            if self.move_direction < 0:
                self.image = self.walk_images_left[self.walk_index]
            else:
                self.image = self.walk_images_right[self.walk_index]
        red = (255,0,0)
        rect = pygame.Rect(self.rect.x+4, self.rect.y+4, self.rect.width-8, self.rect.height-8)
        pygame.draw.rect(screen,red,rect,2)


