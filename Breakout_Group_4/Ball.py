import pygame
import random
from Paddle import Paddle


class Ball:
    radius = 10

    def __init__(self, x_loc, y_loc, dx, dy, colour):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.radius = Ball.radius
        self.dx = dx
        self.dy = dy
        self.colour = colour
        self.acc = 1.0001

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.colour, [self.x_loc, self.y_loc], Ball.radius)

    def detect_colisions(self, objects):
        col_objects = map(Paddle.get_rect, objects)
        col_rects = pygame.Rect(self.x_loc, self.y_loc, 10, 10)
        collide = col_rects.collidelist(list(col_objects))
        if collide != -1:
            # self.dx = -self.dx
            self.dy = -self.dy

    # def collision_paddle(self, paddles):
    #     col_paddles = map(Paddle.get_rect, paddles)
    #     col_rect = pygame.Rect(self.x_loc, self.y_loc, 10, 10)
    #     collide = col_rect.collidelist(list(col_paddles))
    #     if collide != -1:
    #         # self.dx = -self.dx
    #         self.dy = -self.dy

    def init_movement(self):
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

    def update_ball(self, width, height):
        if self.x_loc < 0:
            self.dx = -self.dx
        if self.x_loc > width:
            self.dx = -self.dx
        if self.y_loc < 0:
            self.dy = -self.dy
        if self.y_loc > height:
            #lose
            pass

        #possibility for accelleration to make it more difficult!
        # self.dx *= self.acc
        # self.dy *= self.acc

        self.x_loc += self.dx
        self.y_loc += self.dy
