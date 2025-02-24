import pygame

class Brick:

    # Brick class attributes
    color = (0, 0, 0)
    x = 0
    y = 0
    width = 0
    height = 0
    collider = None

    # Constructor
    def __init__(self, x, y, rgb):
        # Location
        self.x = x
        self.y = y

        # Size (hard coded)
        self.width = 65
        self.height = 20
        
        # Collider
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)

        # If parameter passed in is a triple...
        if (isinstance(rgb, tuple) and len(rgb) == 3):
            # Initialize color
            self.color = rgb
        else:
            print("Invalid brick color variable! Make sure it is a triple (r, g, b)!")

    # Method for drawing the brick
    def draw_brick(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)

    # Getter for the width of the brick
    def get_width(self):
        return self.width
    
    # Getter for the height of the brick
    def get_height(self):
        return self.height
    
    # Getter for the collider of the brick
    def get_collider(self):
        return self.collider