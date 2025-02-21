import pygame


class Ball:
    radius = 10

    def __init__(self, x_loc, y_loc, dx, dy, colour):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.radius = Ball.radius
        self.dx = dx
        self.dy = dy
        self.colour = colour

    def draw_ball(self, screen):
        pass

    def update_ball(self, pressed_keys):
        pass