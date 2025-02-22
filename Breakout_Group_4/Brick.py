import pygame

class Brick:

    # Position of the brick is the top left corner of it
    # Since that is how rectangles are drawn in pygame
    color = (255, 255, 255)
    surface = None
    position_x = 0
    position_y = 0
    width = 0
    height = 0

    def __init__(self, surface, x, y, rgb):
        self.surface = surface
        self.position_x = x
        self.position_y = y
        self.width = 65
        self.height = 20

        if (isinstance(rgb, tuple) and len(rgb) == 3):
            self.color = rgb
        else:
            print("Invalid brick color variable! Make sure it is a triple (r, g, b)!")

    def render(self):
        rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, rect)

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_rect(self):
        return pygame.Rect(self.position_x, self.position_y, self.width, self.height)