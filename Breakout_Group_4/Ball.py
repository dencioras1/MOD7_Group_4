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
        pygame.draw.circle(screen, self.colour, self.x_loc, self.y_loc, Ball.radius)

    def collision_paddle(self, collider):
        # collide = Ball.collideobjects(collider)
        # if collide:
        #     self.dx = -self.dx
        #     self.dy = -self.dy
        pass

    def update_ball(self):
        pass