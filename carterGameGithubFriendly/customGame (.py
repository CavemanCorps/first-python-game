import pygame
import time
import random
import os

# CREATED WINTER OF 2019, AGE 16

#os.chdir(r"C:\Coding Shit\myPrograms\Personal Projects\customGame")
'''PYGAME VARIABLES'''

pygame.init()

display_width = 800
display_height = 600

purple = (160, 32, 240)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
car_height = 50
car_width = 110

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()

'''IMAGES'''

image = pygame.image.load("penis (2020_05_16 22_06_50 UTC).png")
#enemyImages = ['carter.png']
#enemyImage = pygame.image.load('carter (2020_05_16 22_06_50 UTC).png')
enemyImage = pygame.image.load('sheep (2020_05_16 22_06_50 UTC).png')

'''DISPLAY TEXT'''


def text_objects(text, font):
    textSurface = font.render(text, True, green)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()


def score_display(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("WARRENS EMANCIPATED: " + str(count), False, green)
    gameDisplay.blit(text, (2, 2))


def crash():
    message_display('GAME OVER')


'''FUNCTIONS'''


def character(x, y):
    gameDisplay.blit(image, (x, y))


def bullets(coordx, coordy, width, height, color):
    pygame.draw.rect(gameDisplay, color, [coordx, coordy, width, height])


def baddies(coordx, coordy):
    gameDisplay.blit(enemyImage, (coordx, coordy))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


'''GAME LOGIC'''


def game_loop():
    x = (display_width * 0.03)
    y = (display_height * 0.8)

    y_change = 0

    bullet_starty = y + 25
    bullet_startx = display_width * 0.1
    bullet_width = 50
    bullet_height = 7
    bullet_speed = 7

    baddy_starty = random.randrange(0, display_height)
    baddy_startx = 500
    baddy_height = 100
    baddy_speed = -5

    kills = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        '''ASSETS'''

        y += y_change
        gameDisplay.fill(purple)

        # bullets(coordx, coordy, width, height, color)
        bullets(bullet_startx, bullet_starty, bullet_width, bullet_height, green)
        bullet_startx += bullet_speed

        # def baddies(coordx, coordy):
        baddies(baddy_startx, baddy_starty)
        baddy_startx += baddy_speed

        character(x, y)
        score_display(kills)                                        # DISPLAY KILLS

        '''GAME LOGIC'''

        if y > display_height - car_height or y < 0:
            crash()

        if baddy_startx < display_width * -.1:
            baddy_startx = display_width + 1
            baddy_starty = random.randrange(0, display_height)

            baddy_speed += -0.5
            bullet_speed += 1

        if bullet_startx > display_width:
            bullet_starty = y + 25
            bullet_startx = display_width * 0.1

        if bullet_startx + bullet_width > baddy_startx:
            if bullet_starty < baddy_starty + baddy_height and bullet_starty + bullet_height > baddy_starty:
                baddy_startx = display_width + 1
                kills += 1                                          # KILLS ADD 1
                baddy_starty = random.randrange(0, display_height)

        if x + car_width > baddy_startx:
            #print('x crossover')
            if y < baddy_starty + baddy_height and y + car_height > baddy_starty:
                print('y crossover')
                crash()

        pygame.display.update()
        clock.tick(200)


game_loop()
pygame.quit()
quit()
