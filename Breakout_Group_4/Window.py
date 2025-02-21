import pygame

class Window:
    
    # Class attributes

    FRAMERATE = 0
    BACKGROUND = (0, 0, 0)
    WINDOW_SIZE = (0, 0)
    screen = None
    clock = None

    # Constuctor

    def __init__(self, height, width, framerate, rgb):
        self.WINDOW_SIZE = (height, width)
        self.FRAMERATE = framerate

        if(isinstance(rgb, tuple) and len(rgb) == 3):
            self.BACKGROUND = rgb
        else: 
            print('Invalid background color variable! Make sure it is a triple (r, g, b)!')

    def initialize_window(self):

        # Code for game window settings

        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        # Set name for game window

        pygame.display.set_caption('BREAKOUT - G4')

    def check_exit_window(self):

        # Check if the game window is closed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                pygame.quit()

    def fill_background(self):

        # Fill screen with background color

        self.screen.fill(self.BACKGROUND)

    def update_canvas(self):

        # Updating game canvas/window

        pygame.display.flip()

        # Limiting framerate

        self.clock.tick(self.FRAMERATE)

    def get_surface(self):
        return self.screen