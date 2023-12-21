# Imports the modules used: pygame, sys, and random
import pygame, sys
import random

"""
This is the script for the Pong Game! More comments like this will be shown to guide you through the code! Thank you
"""


# Initialises pygame
pygame.init()

# Sets your score and opponent's score
player_score = 0
opponent_score = 0

# Displays the score at the top of the screen using cancatanation
def display_score():
    score_display = score_font.render(str(opponent_score) + '-' + str(player_score), True, (200,200,200))
    screen.blit(score_display,(475,50))


# Animates the ball by changing x position by x speed and y position by y speed
def ball_animation():
    global ball_speed_x, ball_speed_y
    global player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    
    # Checks for collisions with edges of screen
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # Checks if ball passes by the player and calls ball restart() function
    if ball.left <= 0:
        ball_restart()
        player_score = player_score + 1

    if ball.right >= SCREEN_WIDTH:
        ball_restart()
        opponent_score = opponent_score + 1

    # Checks if ball collides with player
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


# Player movement function (called in game loop later in the script)
def player_animation():
    
    # Checks if player collides with edges of the screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


# The opponent ai. This can be changed to a 2 player game by deleting this and making a separate player_animation function for the opponent
def opponent_ai():
    
    # If the ball is above the opponent, the opponent moves up, and if the ball is below the opponent, the opponent moves down (it's that simple lol)
    if opponent.top < ball.y:
        opponent.top += 7

    if opponent.bottom >= ball.y:
        opponent.bottom -= 7
    
    # Checks if the opponent collides with edges of the screen
    if opponent.top <= 0:
        opponent.top = 0

    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT
    





# Ball restart function that restarts the ball at the center if either player scores
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
    pygame.time.delay(400)
    


# Defines the font for the game (it is just the default font of Python
score_font = pygame.font.Font(None, 50)


    


# General setup
pygame.init()

# Game clock which sets the FPS rate
clock = pygame.time.Clock()

# Setting up screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(SCREEN_WIDTH/2 - 15,SCREEN_HEIGHT/2 - 15,30,30)
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - 70,10,80)
opponent = pygame.Rect(20, SCREEN_HEIGHT/2 - 70,10,80)

# Draw Rectangles
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))


player_speed = 0

opponent_speed = 7


# Game Loop
while player_score < 10 and opponent_score < 10:
    for event in pygame.event.get():
        # Checking if the player exits the game with the x at the top right
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Checking for user input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 7

            if event.key == pygame.K_UP:
                player_speed = -7
        else:
            player_speed = 0

        



    # Calling functions
    ball_animation()
    player.y += player_speed

    player_animation()


    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (SCREEN_WIDTH/2,0), (SCREEN_WIDTH/2,SCREEN_HEIGHT))

    # Displaying score at the top of the screen
    display_score()

    

    # Updating display and setting framerate
    pygame.display.flip()
    clock.tick(60)

# Checking if anybody won and printing that in the console
if player_score >= 10:
    print('You Win!')
elif opponent_score >= 10:
    print('You Lose!')

# Exiting the game
pygame.quit()
sys.exit()
