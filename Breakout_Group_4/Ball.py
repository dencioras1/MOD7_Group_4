import pygame
import random
from Paddle import Paddle
from Brick import Brick

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

    def collision_paddle(self, paddles):
        col_paddles = map(Paddle.get_rect, paddles)
        col_rect = pygame.Rect(self.x_loc, self.y_loc, 10, 10)
        collide = col_rect.collidelist(list(col_paddles))
        if collide != -1:
            # self.dx = -self.dx
            self.dy = -self.dy

    def collision_bricks(self, bricks):
        ball_rect = pygame.Rect(self.x_loc - self.radius, self.y_loc - self.radius, self.radius * 2, self.radius * 2)
        
        for brick in bricks:
            brick_rect = brick.get_rect()
            if ball_rect.colliderect(brick_rect):
                # Calculate overlap
                overlap = ball_rect.clip(brick_rect)
                
                if overlap.width < overlap.height:
                    # Left or right collision
                    self.dx = -self.dx
                    if self.x_loc < brick_rect.centerx:
                        self.x_loc = brick_rect.left - self.radius
                    else:
                        self.x_loc = brick_rect.right + self.radius
                else:
                    # Top or bottom collision
                    self.dy = -self.dy
                    if self.y_loc < brick_rect.centery:
                        self.y_loc = brick_rect.top - self.radius
                    else:
                        self.y_loc = brick_rect.bottom + self.radius
                
                return brick

    # def collision_bricks(self, bricks):
    #     for brick in bricks:
    #         if pygame.Rect(self.x_loc, self.y_loc, 10, 10).colliderect(brick.get_rect()):
    #             self.dy = -self.dy
    #             return brick
    #     return None

    def init_movement(self):
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

    def update_ball(self, width, height):
        if self.x_loc < 30:
            self.dx = -self.dx
        if self.x_loc > width - 30:
            self.dx = -self.dx
        if self.y_loc < 30:
            self.dy = -self.dy
        if self.y_loc > height:
            #lose
            pass

        #possibility for accelleration to make it more difficult!
        # self.dx *= self.acc
        # self.dy *= self.acc

        self.x_loc += self.dx
        self.y_loc += self.dy
