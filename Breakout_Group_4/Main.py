import pygame
from Paddle import Paddle
from Ball import Ball
from Board import Board
from Window import Window

def main():

    BALL_SPEED = 1

    score = 0

    FRAMERATE = 120
    BACKGROUND = (0, 0, 0)
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720
    SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    RED = (247, 74, 74)
    BLUE = (74, 129, 247)
    WHITE = (255, 255, 255)

    PADDLES = [Paddle(150, 600, 5, [pygame.K_LEFT, pygame.K_RIGHT], RED),
               Paddle(850, 600, 5, [pygame.K_a, pygame.K_d], BLUE)]
    BALLS = [Ball(WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2, 10, BALL_SPEED, WHITE),
             Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 10, BALL_SPEED, WHITE),
             Ball(WINDOW_WIDTH / 3 * 2, WINDOW_HEIGHT / 2, 10, BALL_SPEED, WHITE)]

    # Code for game window settings
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()

    # Set name for game window
    pygame.display.set_caption('BREAKOUT - G4')
    WINDOW = Window(1080, 720, 120, (0, 0, 0))

    WINDOW.initialize_window()

    BOARD = Board(WINDOW.get_surface())

    # Initialize font for displaying the score / speed
    pygame.font.init()
    FONT = pygame.font.SysFont("consolas", 24)

    # Main loop for the Breakout game

    while(True):

        # Check if the game window is closed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                pygame.quit()

        # Fill screen with background color
        SCREEN.fill(BACKGROUND)
        keys = pygame.key.get_pressed()

        WINDOW.check_exit_window()

        # Game logic goes here

        WINDOW.fill_background()

        BOARD.draw_frame()
        BOARD.draw_bricks()

        for paddle in PADDLES:
            paddle.move_paddle(keys)
            paddle.draw_paddle(SCREEN)

        BALLS[0].collision_paddle(PADDLES)
        BALLS[1].collision_paddle(PADDLES)
        BALLS[2].collision_paddle(PADDLES)

        hit_brick_1 = BALLS[0].collision_bricks(BOARD.get_bricks())
        hit_brick_2 = BALLS[1].collision_bricks(BOARD.get_bricks())
        hit_brick_3 = BALLS[2].collision_bricks(BOARD.get_bricks())

        if hit_brick_1 is not None:
            BOARD.remove_brick(hit_brick_1)
            score += 1
        if hit_brick_2 is not None:
            BOARD.remove_brick(hit_brick_2)
            score += 1
        if hit_brick_3 is not None:
            BOARD.remove_brick(hit_brick_3)
            score += 1

        BALLS[0].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS[1].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS[2].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)

        BALLS[0].draw_ball(SCREEN)
        BALLS[1].draw_ball(SCREEN)
        BALLS[2].draw_ball(SCREEN)
        
        score_surface = FONT.render("Bricks broken: " + str(score), True, (255, 255, 255))
        speed_surface = FONT.render("Current ball speed: " + str(BALLS[0].get_speed()), True, (255, 255, 255))
        SCREEN.blit(score_surface, (30, 30))
        SCREEN.blit(speed_surface, (30, 50))

        WINDOW.update_canvas()

if __name__ == "__main__":
    main()
