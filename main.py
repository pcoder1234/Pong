import pygame, sys
import random

pygame.init()

player_score = 0
opponent_score = 0

def display_score():
    score_display = score_font.render(str(opponent_score) + '-' + str(player_score), True, (200,200,200))
    screen.blit(score_display,(475,50))



def ball_animation():
    global ball_speed_x, ball_speed_y
    global player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.left <= 0:
        ball_restart()
        player_score = player_score + 1

    if ball.right >= SCREEN_WIDTH:
        ball_restart()
        opponent_score = opponent_score + 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1



def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT



def opponent_ai():
    
    if opponent.top < ball.y:
        opponent.top += 7

    if opponent.bottom >= ball.y:
        opponent.bottom -= 7

    if opponent.top <= 0:
        opponent.top = 0

    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT
    






def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
    pygame.time.delay(400)
    



score_font = pygame.font.Font(None, 50)


    


# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up screen
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

while player_score < 10 and opponent_score < 10:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 7

            if event.key == pygame.K_UP:
                player_speed = -7
        else:
            player_speed = 0

        




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

    display_score()

    


    pygame.display.flip()
    clock.tick(60)

if player_score >= 10:
    print('You Win!')
elif opponent_score >= 10:
    print('You Lose!')


pygame.quit()
sys.exit()
