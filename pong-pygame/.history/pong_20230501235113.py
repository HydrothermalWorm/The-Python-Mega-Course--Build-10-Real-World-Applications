import pygame, sys

# general setup
pygame.init()
clock=pygame.time.Clock()

# setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# game rectangles
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.Rect(10,screen_height/2-70,10,140)
opponent = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
court = pygame.Rect(screen_width/2-15,screen_height/2-15,60,60)

# base speed
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

# ball animation
def ball_animation():
    
    global ball_speed_x, ball_speed_y

    # ball delta
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # boundary collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1





while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_w:
                

    ball_animation()

    # visuals
    screen.fill('black')
    pygame.draw.circle(screen,(200,200,200),radius=100, center=(screen_width/2,screen_height/2))
    pygame.draw.circle(screen,'black',radius=99, center=(screen_width/2,screen_height/2))
    pygame.draw.aaline(screen,(200,200,200),(screen_width/2,0), (screen_width/2, screen_height))
    pygame.draw.rect(screen,'orange',player)
    pygame.draw.rect(screen,'cyan',opponent)
    pygame.draw.ellipse(screen,'white',ball)
    

    # updating the window
    pygame.display.flip()
    clock.tick(60)



