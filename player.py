import pygame
from constants import *
from rectangle import Rectangle

class Player(Rectangle):
    def __init__(self,x,y,width,height,speed,color):
        super().__init__(x,y,width,height,speed,color)
        self.gravity = 1
        self.jump_height = -15
        self.velocity = self.jump_height
        self.jumping = False
    
    def draw(self,screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen,self.color,rect)
    
    def update(self):
        self.handle_movement()
        self.handle_jump()


    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.velocity = self.jump_height

        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
    
    def handle_jump(self):
        if self.jumping:
            self.y += self.velocity
            self.velocity += self.gravity
        if self.y > SCREEN_HEIGHT-self.height:
            self.y = SCREEN_HEIGHT-self.height
            self.jumping = False
            self.velocity = 0

    