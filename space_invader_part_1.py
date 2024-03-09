import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (370, 480))

running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow key is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke is released")

    player(playerX, playerY)
    pygame.display.update()