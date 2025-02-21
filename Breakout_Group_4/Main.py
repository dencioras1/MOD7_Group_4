import pygame
from Board import Board
from Window import Window

def main():

    # Object for the game window
    # Window(window_height, window_width, FPS, RGB)

    window = Window(1080, 720, 120, (0, 0, 0))

    window.initialize_window()

    board = Board(window.get_surface())

    # Main loop for the Breakout game

    while(True):

        window.check_exit_window()

        # Game logic goes here

        window.fill_background()

        board.render_frame()
        board.render_bricks()
        
        window.update_canvas()

if __name__ == "__main__":
    main()
