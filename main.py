import pygame
import pygame.sprite
from constants import *
from player import Player
from world import World
from skeleton import skelly_group
from lava import lava_group
from coin import coin_group
from door import door_group
from button import Button

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(50,SCREEN_HEIGHT-101,40,40,"red")
    world = World(WORLD_DATA)
    clock = pygame.time.Clock()
    FPS = 60

    #Images
    back_img = pygame.image.load("images/bg_PNG.png")
    bg_img = pygame.transform.scale(back_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
    restart_img = pygame.image.load("images/Restart_PNG.png")
    start_img = pygame.image.load("images/start_PNG.png")
    exit_img = pygame.image.load("images/exit_PNG.png")

    #buttons
    restart_button = Button(SCREEN_WIDTH//2-150,SCREEN_HEIGHT//2-50,restart_img)
    start_button = Button(SCREEN_WIDTH//2-450,SCREEN_HEIGHT//2,start_img)
    exit_button = Button(SCREEN_WIDTH//2+150,SCREEN_HEIGHT//2,exit_img)

    #condition variables
    coinCount = 0
    game_over = False
    won_game_yet = False
    start_game = False

    #colors
    red = (255,0,0)
    blue = (0,0,255)

    #font related
    scoreFont = pygame.font.SysFont("ubuntu",48)
    font = pygame.font.Font(None,72)
    text_surface = font.render("You Won", True, blue)
    text_rect = text_surface.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_WIDTH // 4)


    while(True):
        clock.tick(FPS)
        screen.fill("black")
        screen.blit(bg_img,(0,0))

        # if the game has started
        if start_game:
            # draws the world and player class
            world.draw(screen)
            player.draw(screen)
            #checks if the game hasnt been won yet, checks if the game is over
            if won_game_yet == False:
                game_over = player.update(screen,world.tile_list)
            #if its over, show the restart button
            if game_over == True:
                # Display restart button over screen
                coinCount = 0
                if restart_button.draw(screen):
                    player.reset(50,SCREEN_HEIGHT-101,20,50,"red")
                    coin_group.empty()
                    skelly_group.empty()
                    world.reset_level(WORLD_DATA)
                    game_over = False  
            #draw the lava 
            lava_group.draw(screen)
            #if the game isnt over, keep the skeleton moving
            if game_over == False and won_game_yet == False:
                skelly_group.update(screen)
            #draw the skeleton and coins
            skelly_group.draw(screen)
            coin_group.draw(screen)
            coin_group.update()
            if pygame.sprite.spritecollide(player, coin_group,True):
                coinCount += 1
            draw_text("x"+ str(coinCount),screen,scoreFont,(255,0,0),100,0)

            door_group.draw(screen)
            door_collide = pygame.sprite.spritecollide(player,door_group,False)
            if door_collide:
                won_game_yet = True
                screen.blit(text_surface,text_rect)


        else:
            start_game = start_button.draw(screen)
            exit_val = exit_button.draw(screen)
            if exit_val:
                return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return      
            
        pygame.display.flip()

def draw_grid(screen):
    for line in range(0,int(SCREEN_HEIGHT/TILE_SIZE)):
        pygame.draw.line(screen,(255,255,255),(0,line*TILE_SIZE),(SCREEN_WIDTH,line*TILE_SIZE))
    for line in range(0,int(SCREEN_WIDTH/TILE_SIZE)):
        pygame.draw.line(screen,(255,255,255),(line*TILE_SIZE,0),(line*TILE_SIZE,SCREEN_HEIGHT))

def draw_text(text,screen,text_font,color,x,y,):
    img = text_font.render(text,True,color)
    screen.blit(img,(x,y))

if __name__ == "__main__":
    main()

