import pygame
from sys import exit
from random import choice

# Game Variables
width = 1366
height = 738
ball_speed_x = choice([-5,-4,-3,3,4,5])
ball_speed_y = choice([-3,-2,-1,1,2,3])
player_speed = 0
opponent_speed = 5
score_point = [0,0]
is_playing = True

pygame.init()

screen = pygame.display.set_mode( (width,height) )
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
font = pygame.font.SysFont('ariel', 70)

ball = pygame.Rect(width/2-10, height/2-10, 20,20)
player = pygame.Rect(width-20, height/2-70, 10,140 )
opponent = pygame.Rect(10, height/2-70, 10,140 )

score = font.render('You Lose',True, 'Red')
score_rect = score.get_rect( center = (width/2,100) )

def ball_reset():
    global ball_speed_x,ball_speed_y
    ball.midtop = (width/2,height/2-10)
    ball_speed_x = choice([-5,-4,-3,3,4,5])
    ball_speed_y = choice([-3,-2,-1,1,2,3])

while True:

    # Event Loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and is_playing:
            if event.key == pygame.K_UP:
                player_speed = -10
                # print('up')
            if event.key == pygame.K_DOWN:
                player_speed = 10
        if event.type == pygame.KEYUP:
            player_speed = 0    

        if not(is_playing):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_playing = True
        

    # Player Movement

    player.y += player_speed

    if player.bottom >= height :    player.bottom = height
    if player.top <= 0 :            player.top = 0

    if opponent.bottom >= height :    opponent.bottom = height
    if opponent.top <= 0 :            opponent.top = 0

    if opponent.top < ball.y :    opponent.top += opponent_speed
    else:    opponent.bottom -= opponent_speed

    # Ball Movement

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball Collision

    if ball.colliderect(player) :       ball_speed_x = -(ball_speed_x)
    if ball.colliderect(opponent) :     ball_speed_x = abs(ball_speed_x)

    if ball.top <= 0 :              ball_speed_y = abs(ball_speed_y)
    if ball.bottom >= height:       ball_speed_y = -(ball_speed_y) 

    # Scoring Condition

    if ball.right < 0 :
        score_point[0]+=1
        ball_reset()
    if ball.left > width :
        score_point[1]+=1
        ball_reset()

    # Stop Condition

    screen.fill('black')

    if score_point[0] == 3 or score_point[1] == 3:
        is_playing = False

        screen.blit(score,score_rect)
    
    else:

        pygame.draw.rect(screen,'White',player)
        pygame.draw.ellipse(screen,'White',ball)
        pygame.draw.rect(screen,'White',opponent)
        pygame.draw.aaline(screen,'beige',(width/2,0),(width/2,height),10)


    pygame.display.update()
    clock.tick(60)

    