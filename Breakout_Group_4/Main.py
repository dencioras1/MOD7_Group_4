import pygame
from Paddle import Paddle
from Ball import Ball
from Board import Board
from Window import Window

def main():

    # Initialize pygame
    pygame.init()

    # Variables that should not be adjusted
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720
    score = 0

    # Variables that can be adjusted
    BALL_SPEED = 1
    PADDLE_RED = (247, 74, 74)
    PADDLE_BLUE = (74, 129, 247)
    WHITE = (255, 255, 255)
    
    # Array for paddle objects
    PADDLES = [Paddle(150, 600, 5, [pygame.K_LEFT, pygame.K_RIGHT], PADDLE_RED),
               Paddle(850, 600, 5, [pygame.K_a, pygame.K_d], PADDLE_BLUE)]
    
    # Array for balls
    BALLS = [Ball(WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2, 10, BALL_SPEED, WHITE),
             Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 10, BALL_SPEED, WHITE),
             Ball(WINDOW_WIDTH / 3 * 2, WINDOW_HEIGHT / 2, 10, BALL_SPEED, WHITE)]

    # Variables related to the game window
    WINDOW = Window(1080, 720, (0, 0, 0))

    # Board variable
    BOARD = Board()

    # Initialize font for displaying the score / speed
    pygame.font.init()
    FONT = pygame.font.SysFont("consolas", 24)
    
    def game_logic(score):
        # Gets keys that are pressed
        keys = pygame.key.get_pressed()
        
        # Move paddles based on the keys being pressed
        for paddle in PADDLES:
            paddle.move_paddle(keys)
        
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
        speed_surface = FONT.render("Current ball speed: " + str(BALLS[0].get_speed()), True, (255, 255, 255))
        WINDOW.get_surface().blit(score_surface, (30, 30))
        WINDOW.get_surface().blit(speed_surface, (30, 50))

        WINDOW.update_canvas()

    # Main loop for the Breakout game ----------------------------------------------------------------------------------------------

    while(True):
        # Check if the game window is closed
        WINDOW.check_exit_window()
        
        score = game_logic(score)

        draw_everything(score)

if __name__ == "__main__":
    main()
