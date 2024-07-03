import pygame
import random

pygame.init()

WIDTH,HIGHT = 800,600
PADDLE_WIDTH,PADDLE_HIEGHT = 10,100
BALL_SIZE = 15
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("My game")

paddle_a = pygame.Rect(50,HIGHT // 2 -PADDLE_HIEGHT // 2,PADDLE_WIDTH,PADDLE_HIEGHT)
paddle_b = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH , HIGHT // 2 - PADDLE_HIEGHT // 2 , PADDLE_WIDTH , PADDLE_HIEGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2 , HIGHT // 2 - BALL_SIZE // 2 ,  BALL_SIZE,BALL_SIZE)

ball_dx = BALL_SPEED_X * random.choice([1,-1])
ball_dy = BALL_SPEED_Y * random.choice([1,-1])

clock = pygame.time.Clock()
running = True

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0 :
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a.bottom < HIGHT :
        paddle_a.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b.top > 0 :
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b.bottom < HIGHT :
        paddle_b.y += PADDLE_SPEED

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= HIGHT :
        ball_dy*= -1
    if ball.left <= 0 or ball.right >= WIDTH :
        ball_dx*= -1

    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_dx *= -1

    if ball.left <= 0 or ball.right >= WIDTH :
        ball = pygame.Rect(WIDTH//2 -BALL_SIZE // 2 , HIGHT // 2 - BALL_SIZE // 2 , BALL_SIZE , BALL_SIZE)
        ball_dx = BALL_SPEED_X * random.choice([1,-1])
        ball_dy = BALL_SPEED_Y * random.choice([1,-1])

    screen.fill(BLACK)
    pygame.draw.rect(screen,WHITE,paddle_a)
    pygame.draw.rect(screen,WHITE,paddle_b)
    pygame.draw.ellipse(screen,WHITE,ball)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()   