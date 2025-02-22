import pygame
from Paddle import Paddle
from Ball import Ball
from Board import Board
from Window import Window

def main():

    # Object for the game window
    # Window(window_height, window_width, FPS, RGB)

    FRAMERATE = 120
    BACKGROUND = (0, 0, 0)
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720
    SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    WHITE = (255, 255, 255)
    PINK = (247, 202, 201)
    PADDLES = [Paddle(150, 600, 5, [pygame.K_LEFT, pygame.K_RIGHT], WHITE),
               Paddle(850, 600, 5, [pygame.K_a, pygame.K_d], PINK)]
    BALL = Ball(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, 0, 0, WHITE)

    # Code for game window settings
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()

    # Set name for game window
    pygame.display.set_caption('BREAKOUT - G4')
    WINDOW = Window(1080, 720, 120, (0, 0, 0))

    WINDOW.initialize_window()

    BOARD = Board(WINDOW.get_surface())
    BALL.init_movement()

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

        BOARD.render_frame()
        BOARD.render_bricks()

        for paddle in PADDLES:
            paddle.update_paddle(keys)
            paddle.draw_paddle(SCREEN)

        BALL.collision_paddle(PADDLES)

        hit_brick = BALL.collision_bricks(BOARD.get_bricks())
        if hit_brick is not None:
            BOARD.remove_brick(hit_brick)

        BALL.update_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALL.draw_ball(SCREEN)
        
        WINDOW.update_canvas()

if __name__ == "__main__":
    main()
