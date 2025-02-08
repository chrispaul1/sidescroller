import pygame
from constants import *

class Player():
    def __init__(self,x,y,width,height,speed,color):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)
        self.speed = speed
        self.color = color
        self.gravity = 1
        self.jump_height = -15
        self.velocity_y = 0
        self.jumped = False
        self.on_platform = False
    
    def draw(self,screen):
        rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        pygame.draw.rect(screen,self.color,rect,2)
    
    def update(self,tiles):
        dx = 0
        dy = 0

        #Handle movement left or right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumped:
            self.velocity_y = self.jump_height
            self.jumped = True

        if keys[pygame.K_RIGHT]:
            dx += self.speed
        
        if keys[pygame.K_LEFT]:
            dx -= self.speed
              
        # handles gravity
        # gravity is always present
        self.velocity_y += self.gravity    
        if self.velocity_y > 10:
            self.velocity_y = 10
        dy += self.velocity_y
    
        # Handles jump
        # if self.jumped:
        #   dy += self.velocity_y

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            dy = 0
            self.jumped = False
            self.velocity_y = 0
        
        #Handles collision
        self.on_platform = False
        for tile in tiles:
            future_rect = pygame.Rect(self.rect.x, self.rect.y+dy, self.width, self.height)
            if tile[1].colliderect(self.rect.x+dx,self.rect.y,self.width,self.height):
                dx=0
            
            if tile[1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                #if the player is falling on top of the platform
                if self.velocity_y >= 0:
                    self.rect.bottom = tile[1].top
                    self.velocity_y = 0
                    self.jumped = False
                    self.on_platform = True
                #if the player is jumped underneath the platform
                elif self.velocity_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.velocity_y = 0
                    self.jumped = True
                    return
                
        # if the player is on a platform, stop any movements in the y-axis       
        if self.on_platform:
            self.jumped = False
            self.velocity_y = 0
            dy = 0

        if not self.on_platform:
            self.jumped = True

        # adds the movements to the x and y coordinates  
        self.rect.x += dx
        self.rect.y += dy
        
