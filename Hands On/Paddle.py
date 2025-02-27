import pygame


class Paddle:
    # Paddle class attributes
    x = 0
    y = 0
    width = 91
    height = 10
    dx = 0
    keys = None
    colour = 0
    collider = None

    # Constructor
    def __init__(self, x, y , dx, keys, colour):
        # Location
        self.x = x
        self.y = y

        # Size
        self.width = Paddle.width
        self.height = Paddle.height

        # Movement direction
        self.dx = dx

        # Keys for controlling paddle 
        self.keys = keys

        # Color and collider
        self.colour = colour
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)

    # Method for drawing paddle
    def draw_paddle(self, surface):
        pygame.draw.rect(surface, self.colour, self.collider)
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height/4))

    # Method for handling movement of the paddle
    def move_paddle(self, pressed_keys):
        if pressed_keys == 1 and self.x > 20:
            # Left
            self.x -= self.dx
        elif pressed_keys == -1 and self.x < 1060 - self.width:
            # Right
            self.x += self.dx
        # else:
        #     # Left
        #     if pressed_keys[self.keys[0]] and self.x > 20:
        #         self.x -= self.dx
        #     # Right
        #     if pressed_keys[self.keys[1]] and self.x < 1060 - self.width:
        #         self.x += self.dx

        # Update collider location
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)

    # Getter for x value
    def get_x(self):
        return self.x
    
    # Getter for width
    def get_width(self):
        return self.width
    
    # Getter for collider
    def get_collider(self):
        return self.collider

