import pygame
from constants import *
from rectangle import Rectangle

class Player(Rectangle):
    def __init__(self,x,y,width,height,speed,color):
        super().__init__(x,y,width,height,speed,color)
        self.gravity = 1.5
        self.jump_height = -15
        self.velocity_y = 0
        self.jumped = False
        self.on_platform = False
    
    def draw(self,screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen,self.color,rect)
    
    def update(self,platforms):
        #Handle movement left or right
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumped and self.velocity_y < 3:
            self.velocity_y = self.jump_height
            self.jumped = True

        if keys[pygame.K_RIGHT]:
            dx += self.speed
        
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        
        self.x += dx
        self.y += dy

        #Handles jump
        if self.jumped:
            self.y += self.velocity_y
        if self.y > SCREEN_HEIGHT-self.height:
            self.y = SCREEN_HEIGHT-self.height
            self.jumped = False
            self.velocity_y = 0
        
        #Handles collision
        next_y = self.y + self.velocity_y
        future_rect = pygame.Rect(self.x,next_y,self.width,self.height)
        self.on_platform = False
        for platform in platforms:
            if future_rect.colliderect(platform.rect):
                #if the player is falling on top of the platform
                if self.velocity_y > 0:
                    self.y = platform.y-self.height
                    self.velocity_y = 0
                    self.jumped = False
                    self.on_platform = True
                #if the player is jumped underneath the platform
                elif self.velocity_y < 0 and next_y <= platform.y+platform.height :
                    self.y = platform.y + platform.height
                    self.velocity_y = 0
                    self.jumped = True
                    return
            
        self.velocity_y += self.gravity    
        if self.velocity_y > 10:
            self.velocity_y = 10    
        if not self.on_platform:
            self.y = next_y
        
    def collideDetection(self, other):
        # Create pygame Rects for collision detection
        self_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        other_rect = pygame.Rect(other.x, other.y, other.width, other.height)
        return self_rect.colliderect(other_rect)