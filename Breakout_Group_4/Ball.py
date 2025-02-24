import pygame
import random
import math
from Paddle import Paddle
from Brick import Brick

class Ball:

    radius = 0
    x_loc = 0
    y_loc = 0
    radius = 0
    dx = 0
    dy = 0
    colour = (0, 0, 0)
    collider = None
    speed = 0

    def __init__(self, x_loc, y_loc, radius, speed, colour):

        self.x_loc = x_loc
        self.y_loc = y_loc
        self.speed = speed
        self.acc = 1.0001

        # Variables dealing with direction
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

        # Normalizing the two variables so that their sum is equal to 1
        length = math.sqrt(self.dx**2 + self.dy**2)
        self.dx /= length
        self.dy /= length

        self.radius = radius
        self.colour = colour
        self.collider = pygame.Rect(self.x_loc - self.radius, self.y_loc - self.radius, self.radius * 2, self.radius * 2)

    def draw_ball(self, screen):

        pygame.draw.circle(screen, self.colour, [self.x_loc, self.y_loc], self.radius)

    def collision_paddle(self, paddles):

        # Update the ball collider location 
        self.update_collider()

        col_paddles = map(Paddle.get_rect, paddles)
        collide = self.collider.collidelist(list(col_paddles))

        if collide != -1:
            # self.dx = -self.dx
            self.adjust_direction(paddles[collide])
            self.dy = -self.dy

    def adjust_direction(self, paddle):
        increment = paddle.get_width() / 7
        # First paddle segment
        if(paddle.get_x() <= self.x_loc and self.x_loc <= paddle.get_x() + increment):
            self.update_direction(-1, 1)
        # Second paddle segment
        elif(paddle.get_x() + increment < self.x_loc and self.x_loc <= paddle.get_x() + 2 * increment):
            self.update_direction(-2, 3)
        # Third paddle segment
        elif(paddle.get_x() + 2 * increment < self.x_loc and self.x_loc <= paddle.get_x() + 3 * increment):
            self.update_direction(-1, 3)
        # Forth (middle) paddle segment
        elif(paddle.get_x() + 3 * increment < self.x_loc and self.x_loc <= paddle.get_x() + 4 * increment):
            self.update_direction(0, 1)
        # Fifth paddle segment
        elif(paddle.get_x() + 4 * increment < self.x_loc and self.x_loc <= paddle.get_x() + 5 * increment):
            self.update_direction(1, 3)
        # Sixth paddle segment
        elif(paddle.get_x() + 5 * increment < self.x_loc and self.x_loc <= paddle.get_x() + 6 * increment):
            self.update_direction(2, 3)
        # Seventh paddle segment
        elif(paddle.get_x() + 6 * increment < self.x_loc and self.x_loc <= paddle.get_x() + 7 * increment):
            self.update_direction(1, 1)
        else:
            pass


    def collision_bricks(self, bricks):

        # Update the ball collider location 
        self.update_collider()        

        for brick in bricks:
            brick_rect = brick.get_rect()
            if self.collider.colliderect(brick_rect):
                # Calculate overlap
                overlap = self.collider.clip(brick_rect)
                
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

    def update_ball(self, width, height):

        # Change x axis movement, depending on which side the ball touches
        if self.x_loc < 30:
            self.dx = -self.dx
        if self.x_loc > width - 30:
            self.dx = -self.dx

        # Same idea except for the y axis, if the ball's y position is higher than 
        if self.y_loc < 30:
            self.dy = -self.dy
        if self.y_loc > height:
            # Lose situation
            pass

        # possibility for acceleration to make it more difficult!
        self.speed *= self.acc
        self.speed *= self.acc

        self.x_loc += self.dx * self.speed
        self.y_loc += self.dy * self.speed

    def update_collider(self):

        self.collider = pygame.Rect(self.x_loc - self.radius, self.y_loc - self.radius, self.radius * 2, self.radius * 2)

    def update_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy
        # Normalizing the two variables so that their sum is equal to 1
        length = math.sqrt(self.dx**2 + self.dy**2)
        self.dx /= length
        self.dy /= length

    def get_speed(self):
        return self.speed