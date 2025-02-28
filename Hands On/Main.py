import pygame
from Paddle import Paddle
from Ball import Ball
from Board import Board
from Window import Window
from support_functions import *

import math

def make_balls(window_width, window_height, ball_speed, colour):
    BALLS = [Ball(window_width / 3, window_height / 2, 10, ball_speed, colour),
             Ball(window_width / 2, window_height / 2, 10, ball_speed, colour),
             Ball(window_width / 3 * 2, window_height / 2, 10, ball_speed, colour)]
    return BALLS

def check_balls(BALLS_BLUE, BALLS_RED, window_width, window_height, ball_speed, blue_color, red_color):
    i = 0
    for ball_blue in BALLS_BLUE:
        if ball_blue.get_state() == 2:
            i += 1
    if i == 3:
        BALLS_BLUE.clear()
        len(BALLS_BLUE)
        BALLS_BLUE = make_balls(window_width, window_height, ball_speed, blue_color)
    j = 0
    for balls_red in BALLS_RED:
        if balls_red.get_state() == 2:
            j += 1
    if j == 3:
        BALLS_RED.clear()
        BALLS_RED = make_balls(window_width, window_height, ball_speed, red_color)
    
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
    scores = [0, 0] # Red - index 0; Blue - index 1

    # Variables that can be adjusted
    BALL_SPEED = 1
    PADDLE_RED = (247, 74, 74)
    PADDLE_BLUE = (74, 129, 247)
    WHITE = (255, 255, 255)
    
    # Array for paddle objects
    PADDLES = [Paddle(150, 600, 5, [pygame.K_LEFT, pygame.K_RIGHT], PADDLE_RED),
               Paddle(850, 600, 5, [pygame.K_a, pygame.K_d], PADDLE_BLUE)]
    
    # Array for balls
    BALLS_BLUE = make_balls(WINDOW_WIDTH, WINDOW_HEIGHT, BALL_SPEED, PADDLE_BLUE)
    BALLS_RED = make_balls(WINDOW_WIDTH, WINDOW_HEIGHT, BALL_SPEED, PADDLE_RED)

    # Variables related to the game window
    WINDOW = Window(1080, 720, (0, 0, 0))

    # Board variable
    BOARD = Board()

    # TSP variable
    # TSP = TSP()

    # Initialize font for displaying the score / speed
    pygame.font.init()
    FONT = pygame.font.SysFont("consolas", 24)
    
    def game_logic(scores, gl_grid):
        # Gets keys that are pressed
        keys = pygame.key.get_pressed()

        #read grid
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




        # Move paddles based on the keys being pressed
        for paddle in PADDLES:
            paddle.move_paddle(keys)

        if keys[pygame.K_SPACE]:
            for ball_blue in BALLS_BLUE:
                ball_blue.initialize_balls()
            for ball_red in BALLS_RED:
                ball_red.initialize_balls()

        # Check for collisions between the balls and the paddles
        BALLS_BLUE[0].collision_paddle(PADDLES)
        BALLS_BLUE[1].collision_paddle(PADDLES)
        BALLS_BLUE[2].collision_paddle(PADDLES)
        BALLS_RED[0].collision_paddle(PADDLES)
        BALLS_RED[1].collision_paddle(PADDLES)
        BALLS_RED[2].collision_paddle(PADDLES)

        # Bricks hit for each ball
        hit_brick_blue_1 = BALLS_BLUE[0].collision_bricks(BOARD.get_bricks())
        hit_brick_blue_2 = BALLS_BLUE[1].collision_bricks(BOARD.get_bricks())
        hit_brick_blue_3 = BALLS_BLUE[2].collision_bricks(BOARD.get_bricks())
        hit_brick_red_1 = BALLS_RED[0].collision_bricks(BOARD.get_bricks())
        hit_brick_red_2 = BALLS_RED[1].collision_bricks(BOARD.get_bricks())
        hit_brick_red_3 = BALLS_RED[2].collision_bricks(BOARD.get_bricks())

        # Move ball (parameters indicate borders)
        BALLS_BLUE[0].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS_BLUE[1].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS_BLUE[2].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS_RED[0].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS_RED[1].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS_RED[2].move_ball(WINDOW_WIDTH, WINDOW_HEIGHT)

        # If there is a brick hit...
        if hit_brick_blue_1 is not None:
            # Remove it and increment the counter
            BOARD.remove_brick(hit_brick_blue_1)
            scores[0] += 1
        if hit_brick_blue_2 is not None:
            BOARD.remove_brick(hit_brick_blue_2)
            scores[0] += 1
        if hit_brick_blue_3 is not None:
            BOARD.remove_brick(hit_brick_blue_3)
            scores[0] += 1
        if hit_brick_red_1 is not None:
            BOARD.remove_brick(hit_brick_red_1)
            scores[1] += 1
        if hit_brick_red_2 is not None:
            BOARD.remove_brick(hit_brick_red_2)
            scores[1] += 1
        if hit_brick_red_3 is not None:
            BOARD.remove_brick(hit_brick_red_3)
            scores[1] += 1
        return scores

    def draw_everything(scores):
        WINDOW.fill_background()

        BOARD.draw_frame(WINDOW.get_surface())
        BOARD.draw_bricks(WINDOW.get_surface())

        BALLS_BLUE[0].draw_ball(WINDOW.get_surface())
        BALLS_BLUE[1].draw_ball(WINDOW.get_surface())
        BALLS_BLUE[2].draw_ball(WINDOW.get_surface())

        BALLS_RED[0].draw_ball(WINDOW.get_surface())
        BALLS_RED[1].draw_ball(WINDOW.get_surface())
        BALLS_RED[2].draw_ball(WINDOW.get_surface())

        PADDLES[0].draw_paddle(WINDOW.get_surface())
        PADDLES[1].draw_paddle(WINDOW.get_surface())

        score_blue_surface = FONT.render("Blue score: " + str(scores[0]), True, (255, 255, 255))
        score_red_surface = FONT.render("Red score: " + str(scores[1]), True, (255, 255, 255))
        speed_surface = FONT.render("Current ball speed: " + str(math.ceil(BALLS_RED[0].get_speed() * 100) / 100), True, (255, 255, 255))

        WINDOW.get_surface().blit(score_blue_surface, (30, 30))
        WINDOW.get_surface().blit(score_red_surface, (850, 30))
        WINDOW.get_surface().blit(speed_surface, (WINDOW_WIDTH / 2 - 175, 30))

        enter_message = FONT.render("Press SPACE to start the game :)", True, WHITE)
        WINDOW.get_surface().blit(enter_message, (WINDOW_WIDTH/2-200, 690))

        WINDOW.update_canvas()

    # Main loop for the Breakout game ----------------------------------------------------------------------------------------------

    while(True):
        # Check if the game window is closed
        WINDOW.check_exit_window()


        scores = game_logic(scores, grid)
        
        check_balls(BALLS_BLUE, BALLS_RED, WINDOW_WIDTH, WINDOW_HEIGHT, BALL_SPEED, PADDLE_BLUE, PADDLE_RED)

        if len(BALLS_BLUE) != 0 and len(BALLS_RED) != 0:
            draw_everything(scores)


if __name__ == "__main__":
    main()



