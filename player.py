import pygame
from constants import *
from lava import lava_group
from skeleton import skelly_group
from sprite_sheet import get_image

class Player():
    def __init__(self,x,y,width,height,color):
        self.reset(x,y,width,height,color)
    
    def draw(self,screen):
        rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        pygame.draw.rect(screen,self.color,rect,2)
        screen.blit(self.image,self.rect)
        
        

    def update(self,screen,tiles):
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
                self.direction = 1
                self.walk_counter += 1
            
            if keys[pygame.K_LEFT]:
                dx -= 5
                self.direction = -1
                self.walk_counter += 1
            
            if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
                self.walk_index = 0
                self.walk_counter=0
                if self.idle_counter > self.idle_cooldown:
                    self.idle_counter = 0
                if self.idle_index >= len(self.idle_images_right):
                    self.idle_index = 0

                if self.direction == -1:
                    self.image = self.idle_images_left[0]
                else:
                    self.image = self.idle_images_right[0]
                self.idle_counter += 1
                self.idle_index += 1

            #handle animation
            if self.walk_counter > self.walk_cooldown:
                self.walk_counter = 0
                self.walk_index += 1
                if self.walk_index >= len(self.walk_images_right):
                    self.walk_index = 0
                if self.direction == -1:
                    self.image = self.walk_images_left[self.walk_index]
                else:
                    self.image = self.walk_images_right[self.walk_index]

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
                skeletonObjs = pygame.sprite.spritecollide(self,skelly_group,False)
                for obj in skeletonObjs:
                    if self.mask.overlap(obj.mask, (obj.rect.x-self.rect.x,obj.rect.y-self.rect.y)):
                        self.game_over = True
                #get the mask for each picture from the current index 

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
        self.direction = 1
        self.walk_images_right = []
        self.walk_images_left = []
        self.idle_images_right = []
        self.idle_images_left = []
        self.walk_index = 0
        self.idle_index = 0
        self.walk_counter = 0
        self.walk_cooldown = 3
        self.idle_counter = 0
        self.idle_cooldown = 5
        knight_sprite = pygame.image.load("images/knight and dummy idle spritesheet.png").convert_alpha()
        Black=(0,0,0)
        idle_image_right0 = get_image(knight_sprite,0,1,40,40,Black)
        idle_image_left0 = pygame.transform.flip(idle_image_right0,True,False)
        idle_image_left0.set_colorkey(Black)
        idle_image_right1 = get_image(knight_sprite,0,7,40,40,Black)
        idle_image_left1 = pygame.transform.flip(idle_image_right1,True,False)
        idle_image_left1.set_colorkey(Black)


        self.idle_images_right.append(idle_image_right0)
        self.idle_images_right.append(idle_image_right1)
        self.idle_images_left.append(idle_image_left0)
        self.idle_images_left.append(idle_image_left1)

        for i in range(0,4):
            image_right = get_image(knight_sprite,i,11,40,40,Black)
            image_left = pygame.transform.flip(image_right,True,False)
            image_left.set_colorkey(Black)
            self.walk_images_right.append(image_right)
            self.walk_images_left.append(image_left)
        self.image = self.idle_images_right[0]
        self.mask = pygame.mask.from_surface(self.image)

    
    
