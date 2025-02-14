import pygame
from Board import Board

def main():

    # Constant variables

    FRAMERATE = 120
    BACKGROUND = (0, 0, 0)
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720
    SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

    # Code for game window settings

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    board = Board(screen)

    # Set name for game window

    pygame.display.set_caption('BREAKOUT - G4')

    # Main loop for the Breakout game

    while(True):

        # Check if the game window is closed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                pygame.quit()

        # Fill screen with background color
        screen.fill(BACKGROUND)

        # Game logic goes here

        board.render_frame()

        # Updating game canvas/window
        pygame.display.flip()

        # Limiting framerate
        clock.tick(FRAMERATE)

if __name__ == "__main__":
    main()
