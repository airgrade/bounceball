import pygame
from pygame.locals import*
import sys
from pathlib import Path
import random

#2 DEFINE CONSTANTS
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE =3

#3 INITIALIZE THE WOLRD 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 load assets:image(s), sound(s),etc.
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.png')
#5 initialize variables
ballx = random.randrange(MAX_WIDTH)
bally = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

ballRect = pygame.Rect(ballx, bally, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
#6 loop forever
while True:
    
    #7 check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #see if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            #check if the click was in the rect of the ball
            #if so choose a random new location
            if ballRect.collidepoint(event.pos):
                ballx = random.randrange(MAX_WIDTH)
                bally = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballx, bally, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
                
        #see user a pressed a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballx = ballx - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballx = ballx + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                bally = bally - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                bally = bally + N_PIXELS_TO_MOVE
                
                
                
                
    
    #8 Do any "per frame" actions
    #check for users pressing keys
    keyPressedTuple = pygame.key.get_pressed()
    
    if keyPressedTuple[pygame.K_LEFT]: #Moving left
        ballx = ballx -N_PIXELS_TO_MOVE
        
    
    #Check if the ball is collinding with target
    ballRect = pygame.Rect(ballx, bally, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print("Ball is touching the target")
    #9 clear window
    window.fill(BLACK)
    
    #10 Draw all window elements
    #Draw ball at randomized location
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballImage, (ballx, bally))
    
    #Update the window
    pygame.display.update()
    
    #slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
            
            