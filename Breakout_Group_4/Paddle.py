import pygame

class Paddle:

    width = 40
    height = 10

    def __init__(self, x_loc, y_loc , dx, keys, colour):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.width = Paddle.width
        self.height = Paddle.height
        self.dx = dx
        self.keys = keys
        self.colour = colour
    
    def draw_paddle(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x_loc, self.y_loc, self.width, self.height))

    def update_paddle(self, pressed_keys):
        if pressed_keys[self.keys[0]]: ##left movement
            self.x_loc -= self.dx
        if pressed_keys[self.keys[1]]: ##right movement
            self.x_loc += self.dx

    def set_location(self):
        locations = [self.x_loc, self.y_loc]
        return locations

