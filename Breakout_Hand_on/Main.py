import pygame

from Breakout_Hand_on.support_functions import TSPDecoder
from Paddle import Paddle
from Ball import Ball
from Board import Board
from Window import Window
import numpy as np
import math


def make_balls(window_width, window_height, ball_speed, colour):
    BALLS = [Ball(window_width / 3, window_height / 2, 10, ball_speed, colour),
             Ball(window_width / 2, window_height / 2, 10, ball_speed, colour),
             Ball(window_width / 3 * 2, window_height / 2, 10, ball_speed, colour)]
    return BALLS


def main():
    # Initialize pygame
    pygame.init()

    rows = 27
    columns = 19

    TSP = TSPDecoder(rows=rows, columns=columns)
    grid = np.zeros((TSP.rows, TSP.columns))

    # Variables that should not be adjusted
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720
    score = 0

    # Variables that can be adjusted
    BALL_SPEED = 1
    PADDLE_RED = (247, 74, 74)
    PADDLE_BLUE = (74, 129, 247)
    WHITE = (255, 255, 255)
    BALL_COLOUR = (203,115,110)
    
    # Array for paddle objects
    PADDLES = [Paddle(150, 600, 5, [pygame.K_LEFT, pygame.K_RIGHT], PADDLE_RED),
               Paddle(850, 600, 5, [pygame.K_a, pygame.K_d], PADDLE_BLUE)]
    
    # Array for balls
    BALLS = make_balls(WINDOW_WIDTH, WINDOW_HEIGHT, BALL_SPEED, BALL_COLOUR)

    # Variables related to the game window
    WINDOW = Window(1080, 720, (0, 0, 0))

    # Board variable
    BOARD = Board()


    # Initialize font for displaying the score / speed
    pygame.font.init()
    FONT = pygame.font.SysFont("consolas", 24)
    
    def game_logic(score, gl_grid):

        # read grid
        if TSP.frame_available:
            gl_grid = TSP.readFrame()
        # print(pygame.K_LEFT) 1073741904

        for r in range(rows):
            for c in range(columns):
                # Get the value of the grid
                # first paddle red, second blue
                value = gl_grid[r][c]
                if value > 70:
                    if r > 14:
                        if c > 9:
                            # blue paddle to left
                            PADDLES[1].move_paddle(1)
                            print("Left 2")
                        else:
                            # red paddle to right
                            PADDLES[0].move_paddle(-1)
                            print("Right 1")

                    elif r < 14:
                        if c > 9:
                            # blue paddle to right
                            PADDLES[1].move_paddle(-1)
                            print("Right 2")
                        else:
                            # red paddle to left
                            PADDLES[0].move_paddle(1)
                            print("Left 1")
                    else:
                        print("no input")

        # Check for collisions between the balls and the paddles
        BALLS[0].collision_paddle(PADDLES)
        BALLS[1].collision_paddle(PADDLES)
        BALLS[2].collision_paddle(PADDLES)

        # Bricks hit for each ball
        hit_brick_1 = BALLS[0].collision_bricks(BOARD.get_bricks())
        hit_brick_2 = BALLS[1].collision_bricks(BOARD.get_bricks())
        hit_brick_3 = BALLS[2].collision_bricks(BOARD.get_bricks())

        # Move ball (parameters indicate borders)
        BALLS[0].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS[1].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS[2].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)

        # If there is a brick hit...
        if hit_brick_1 is not None:
            # Remove it and increment the counter
            BOARD.remove_brick(hit_brick_1)
            score += 1
        if hit_brick_2 is not None:
            BOARD.remove_brick(hit_brick_2)
            score += 1
        if hit_brick_3 is not None:
            BOARD.remove_brick(hit_brick_3)
            score += 1
        return score

    def draw_everything(score):
        WINDOW.fill_background()

        BOARD.draw_frame(WINDOW.get_surface())
        BOARD.draw_bricks(WINDOW.get_surface())

        BALLS[0].draw_ball(WINDOW.get_surface())
        BALLS[1].draw_ball(WINDOW.get_surface())
        BALLS[2].draw_ball(WINDOW.get_surface())
        
        PADDLES[0].draw_paddle(WINDOW.get_surface())
        PADDLES[1].draw_paddle(WINDOW.get_surface())

        score_surface = FONT.render("Bricks broken: " + str(score), True, (255, 255, 255))
        speed_surface = FONT.render("Current ball speed: " + str(math.ceil(BALLS[0].get_speed() * 100) / 100), True, (255, 255, 255))
        WINDOW.get_surface().blit(score_surface, (30, 30))
        WINDOW.get_surface().blit(speed_surface, (30, 50))

        enter_message = FONT.render("Press SPACE to start the game :)", True, WHITE)

        WINDOW.get_surface().blit(score_surface, (30, 30))
        WINDOW.get_surface().blit(speed_surface, (30, 50))
        WINDOW.get_surface().blit(enter_message, (WINDOW_WIDTH/2-200, 690))

        WINDOW.update_canvas()

    # Main loop for the Breakout game ----------------------------------------------------------------------------------------------

    while(True):
        # Check if the game window is closed
        WINDOW.check_exit_window()

        # Gets keys that are pressed
        keys = pygame.key.get_pressed()


        # Move paddles based on the keys being pressed
        for paddle in PADDLES:
            paddle.move_paddle(keys)

        # Check if the game window is closed
        WINDOW.check_exit_window()

        if keys[pygame.K_SPACE]:
            for ball in BALLS:
                ball.initialize_balls()

        i = 0
        for b in BALLS:
            if b.get_state() == 2:
                i += 1
        if i == 3:
            BALLS.clear()
            BALLS = make_balls(WINDOW_WIDTH, WINDOW_HEIGHT, BALL_SPEED, BALL_COLOUR)

        score = game_logic(score, grid)

        draw_everything(score)


if __name__ == "__main__":
    main()



