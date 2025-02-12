import pygame
from constants import *
from lava import lava_group
from skeleton import skelly_group

class Player():
    def __init__(self,x,y,width,height,color):
        self.reset(x,y,width,height,color)
    
    def draw(self,screen):
        rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        pygame.draw.rect(screen,self.color,rect,2)
    
    def update(self,tiles):
        dx = 0
        dy = 0
        if self.game_over == 0: 
            #Handle movement left or right
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.jumped:
                self.velocity_y = self.jump_height
                self.jumped = True

            if keys[pygame.K_RIGHT]:
                dx += 5
            
            if keys[pygame.K_LEFT]:
                dx -= 5
            # handles gravity
            self.velocity_y += self.gravity    
            if self.velocity_y > 10:
                self.velocity_y = 10
            dy += self.velocity_y

            # Handles jump
            # if self.jumped:
            #   dy += self.velocity_y
                    
            #Handles collision
            self.on_platform = False
            for tile in tiles:
                future_rect = pygame.Rect(self.rect.x, self.rect.y+dy, self.width, self.height)
                if tile[1].colliderect(self.rect.x+dx,self.rect.y,self.width,self.height):
                    #if moving right
                    if dx > 0:
                        self.rect.right = tile[1].left
                    # If moving left
                    elif dx < 0:
                        self.rect.left = tile[1].right
                    dx=0
                
                if tile[1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                    #if the player is falling on top of the platform
                    if self.velocity_y >= 0:
                        dy = tile[1].top - self.rect.bottom
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

            # handle enemy or lava collison
            if pygame.sprite.spritecollide(self,lava_group,False):
                self.game_over = True
            
            if pygame.sprite.spritecollide(self,skelly_group,False):
                self.game_over = True

            # adds the movements to the x and y coordinates  
            self.rect.x += dx
            self.rect.y += dy

            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
                dy = 0
                self.jumped = False
                self.velocity_y = 0
        return self.game_over
            
    def reset(self,x,y,width,height,color):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.gravity = 1
        self.jump_height = -15
        self.velocity_y = 0
        self.jumped = False
        self.on_platform = False
        self.game_over = False
    