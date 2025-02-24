import pygame

class Paddle:

    x = 0
    y = 0
    width = 91
    height = 10
    dx = 0
    keys = None
    colour = 0
    col_rect = None

    def __init__(self, x, y , dx, keys, colour):
        self.x = x
        self.y = y
        self.width = Paddle.width
        self.height = Paddle.height
        self.dx = dx
        self.keys = keys
        self.colour = colour
        self.col_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_paddle(self, screen):
        pygame.draw.rect(screen, self.colour, self.col_rect)

    def update_paddle(self, pressed_keys):
        if pressed_keys[self.keys[0]] and self.x > 20: ##left movement
            self.x -= self.dx
        if pressed_keys[self.keys[1]] and self.x < 1060 - self.width: ##right movement
            self.x += self.dx

        self.col_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def set_location(self):
        locations = [self.x, self.y]
        return locations

    def get_x(self):
        return self.x
    
    def get_width(self):
        return self.width
    
    def get_collider(self):
        return self.col_rect

