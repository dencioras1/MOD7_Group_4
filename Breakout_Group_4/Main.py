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
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    # Set name for game window
    pygame.display.set_caption('BREAKOUT - G4')
    window = Window(1080, 720, 120, (0, 0, 0))

    window.initialize_window()

    board = Board(window.get_surface())
    BALL.init_movement()

    # Main loop for the Breakout game

    while(True):

        # Check if the game window is closed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                pygame.quit()

        # Fill screen with background color
        screen.fill(BACKGROUND)
        keys = pygame.key.get_pressed()

        window.check_exit_window()

        # Game logic goes here


        window.fill_background()

        board.render_frame()
        board.render_bricks()
        for paddle in PADDLES:
            paddle.update_paddle(keys)
            paddle.draw_paddle(screen)

        BALL.collision_paddle(PADDLES)
        BALL.update_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALL.draw_ball(screen)
        
        window.update_canvas()

if __name__ == "__main__":
    main()
