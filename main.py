import pygame
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIDTH_STICK, LEN_STICK = 10, 70
STICK_VEL = 4
BALL_RADIUS = 7
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FORWARD = True
HEALTH_FONT = pygame.font.SysFont('comicsans', 100)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")
FPS = 60

def draw_window(left_stick, right_stick, ball):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, RED, left_stick)
    pygame.draw.rect(WIN, GREEN, right_stick)
    ball = pygame.draw.ellipse(WIN, RED, ball)
    pygame.display.update()
    return ball

def handle_left_stick_movement(keys_pressed, left_stick):
    if keys_pressed[pygame.K_x] and left_stick.y+LEN_STICK < HEIGHT:
        left_stick.y += STICK_VEL
    if keys_pressed[pygame.K_w] and left_stick.y > 0:
        left_stick.y -= STICK_VEL


def handle_right_stick_movement(keys_pressed, right_stick):
    if keys_pressed[pygame.K_DOWN] and right_stick.y+LEN_STICK < HEIGHT:
        right_stick.y += STICK_VEL
    if keys_pressed[pygame.K_UP] and right_stick.y > 0:
        right_stick.y -= STICK_VEL

def handle_ball_movement(ball, left_stick, right_stick, ball_vel_x, ball_vel_y):
    ball.x += ball_vel_x
    ball.y += ball_vel_y
    fail = False
    if ball.colliderect(left_stick) or ball.colliderect(right_stick):
        ball_vel_x *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        fail = True
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel_y *= -1
    return ball_vel_x, ball_vel_y, fail


def main():

    clock = pygame.time.Clock()
    left_stick = pygame.Rect(10, 10, WIDTH_STICK, LEN_STICK)
    ball_x = 50
    ball_y = 40
    ball_vel_x = 7
    ball_vel_y = 5
    right_stick = pygame.Rect(WIDTH-10-WIDTH_STICK, HEIGHT-10-LEN_STICK, WIDTH_STICK, LEN_STICK)
    ball = pygame.Rect(50, 40, 20, 20)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_left_stick_movement(keys_pressed, left_stick)
        handle_right_stick_movement(keys_pressed, right_stick) 
        ball_vel_x, ball_vel_y, fail = handle_ball_movement(ball, left_stick, right_stick, ball_vel_x, ball_vel_y)  
        if fail:
            break
        draw_window(left_stick, right_stick, ball)

if __name__ == "__main__":
    main()