import pygame

class Rectangle():
    def __init__(self,x,y,width,height,speed,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(x,y,width,height)
    
    def draw():
        pass


