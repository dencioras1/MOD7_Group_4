import pygame

class Window:
    
    FRAMERATE = 0
    BACKGROUND = (0, 0, 0)
    WINDOW_WIDTH = 0
    WINDOW_HEIGHT = 0
    SIZE = (0, 0)

    # Constuctor

    def __init__(self, height, width, framerate, rgb):
        self.WINDOW_HEIGHT = height
        self.WINDOW_WIDTH = width
        self.FRAMERATE = framerate

    # Constant variables

