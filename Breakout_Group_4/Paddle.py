import pygame

class Paddle:

    width = 91
    height = 10

    def __init__(self, x_loc, y_loc , dx, keys, colour):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.width = Paddle.width
        self.height = Paddle.height
        self.dx = dx
        self.keys = keys
        self.colour = colour
        self.col_rect = pygame.Rect(self.x_loc, self.y_loc, self.width, self.height)

    def draw_paddle(self, screen):
        pygame.draw.rect(screen, self.colour, self.col_rect)

    def update_paddle(self, pressed_keys):
        if pressed_keys[self.keys[0]] and self.x_loc > 20: ##left movement
            self.x_loc -= self.dx
        if pressed_keys[self.keys[1]] and self.x_loc < 1060 - self.width: ##right movement
            self.x_loc += self.dx

        self.col_rect = pygame.Rect(self.x_loc, self.y_loc, self.width, self.height)

    def set_location(self):
        locations = [self.x_loc, self.y_loc]
        return locations

    def get_x(self):
        return self.x_loc
    
    def get_width(self):
        return self.width
    
    def get_collider(self):
        return self.col_rect

