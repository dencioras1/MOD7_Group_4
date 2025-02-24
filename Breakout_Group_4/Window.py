import pygame

class Window:
    
    # Window class attributes
    BACKGROUND = (0, 0, 0)
    WINDOW_SIZE = (0, 0)
    SURFACE = None

    # Constuctor
    def __init__(self, height, width, rgb):
        # Window size
        self.WINDOW_SIZE = (height, width)

        # Screen / Surface
        self.SURFACE = pygame.display.set_mode(self.WINDOW_SIZE)

        # Set name for game window
        pygame.display.set_caption('BREAKOUT - G4')

        # If rgb parameter is a triple...
        if(isinstance(rgb, tuple) and len(rgb) == 3):
            # Set the background color
            self.BACKGROUND = rgb
        else: 
            print('Invalid background color variable! Make sure it is a triple (r, g, b)!')

    # Method for checking the game window is closed
    def check_exit_window(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    # Method for coloring in the background
    def fill_background(self):
        self.SURFACE.fill(self.BACKGROUND)

    # Method for updating the game window
    def update_canvas(self):
        pygame.display.flip()

    # Getter for the surface
    def get_surface(self):
        return self.SURFACE