import pygame

pygame.init()

## initialize the pygame ##

## create the screen ##
screen = pygame.display.pygame.display.set_mode((800, 600))

running = True
while running:
    for event in python.event.get():
        if event.type == pygame.quit():
            running = False
