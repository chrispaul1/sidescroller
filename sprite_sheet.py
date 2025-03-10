import pygame
def get_image(sheet,frame,row,width,height,color):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet,(0,0),(frame*width,row*8,width,height))
    image = pygame.transform.scale(image,(50,50))
    image.set_colorkey((0,0,0))
    return image