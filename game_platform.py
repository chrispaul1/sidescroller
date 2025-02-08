import pygame
from rectangle import Rectangle

class Platform(Rectangle):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height,0,"green")

    def draw(self,screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen,self.color,rect)