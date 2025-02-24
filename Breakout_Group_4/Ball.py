import pygame
import random
import math
from Paddle import Paddle
from Brick import Brick

class Ball:

    # Ball class attributes
    x = 0
    y = 0
    speed = 0
    accelaration = 0
    radius = 0
    dx = 0
    dy = 0
    colour = (0, 0, 0)
    collider = None
    state = 0

    # Constructor
    def __init__(self, x, y, radius, speed, colour):
        # Location 
        self.x = x
        self.y = y

        # Speed / accelaration 
        self.speed = speed
        self.accelaration = 1.0001

        # Ball state
        self.state = Ball.state

        # Variables dealing with direction
        self.dx = Ball.dx
        self.dy = Ball.dy

        # Normalizing the two variables so that their sum is equal to 1
        if self.state == 1:
            length = math.sqrt(self.dx**2 + self.dy**2)
            self.dx /= length
            self.dy /= length

        # Ball size, color and collider
        self.radius = radius
        self.colour = colour
        self.collider = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    # Method for drawing the ball
    def draw_ball(self, surface):
        pygame.draw.circle(surface, self.colour, [self.x, self.y], self.radius)
        pygame.draw.circle(surface, (255, 255, 255), [self.x-5, self.y-4], self.radius/4)

    # Method for handling collisions with the paddles
    def collision_paddle(self, paddles):
        self.update_collider()

        # Get paddle colliders
        paddle_colliders = map(Paddle.get_collider, paddles)

        # check which paddles have been collided with
        collided = self.collider.collidelist(list(paddle_colliders))

        # If there is a collision...
        if collided != -1:
            self.adjust_direction(paddles[collided])

    # Method for adjust the direction of the ball, based on where it bounces off of a paddle
    # Each paddle is divided into 7 segments
    # 1st segment - 45 degrees left
    # 7th segment - 45 degrees right
    # Increments of 15 degrees
    def adjust_direction(self, paddle):
        increment = paddle.get_width() / 7
        # First paddle segment
        if(paddle.get_x() <= self.x and self.x <= paddle.get_x() + increment):
            self.update_direction(-1, -1)
        # Second paddle segment
        elif(paddle.get_x() + increment < self.x and self.x <= paddle.get_x() + 2 * increment):
            self.update_direction(-2, -3)
        # Third paddle segment
        elif(paddle.get_x() + 2 * increment < self.x and self.x <= paddle.get_x() + 3 * increment):
            self.update_direction(-1, -3)
        # Forth (middle) paddle segment
        elif(paddle.get_x() + 3 * increment < self.x and self.x <= paddle.get_x() + 4 * increment):
            self.update_direction(0, -1)
        # Fifth paddle segment
        elif(paddle.get_x() + 4 * increment < self.x and self.x <= paddle.get_x() + 5 * increment):
            self.update_direction(1, -3)
        # Sixth paddle segment
        elif(paddle.get_x() + 5 * increment < self.x and self.x <= paddle.get_x() + 6 * increment):
            self.update_direction(2, -3)
        # Seventh paddle segment
        elif(paddle.get_x() + 6 * increment < self.x and self.x <= paddle.get_x() + 7 * increment):
            self.update_direction(1, -1)
        else:
            pass

    # Method for handling collisions with bricks
    def collision_bricks(self, bricks):
        self.update_collider()        

        for brick in bricks:
            brick_collider = brick.get_collider()
            # If ball collides with a brick...
            if self.collider.colliderect(brick_collider):
                # Calculate overlap
                overlap = self.collider.clip(brick_collider)
                if overlap.width < overlap.height:
                    # Left or right collision
                    self.dx = -self.dx
                    if self.x < brick_collider.centerx:
                        # Adjust ball position to match left side of brick
                        self.x = brick_collider.left - self.radius
                    else:
                        # Adjust ball position to match right side of brick
                        self.x = brick_collider.right + self.radius
                else:
                    # Top or bottom collision
                    self.dy = -self.dy
                    if self.y < brick_collider.centery:
                        # Adjust ball position to match top side of brick
                        self.y = brick_collider.top - self.radius
                    else:
                        # Adjust ball position to match bottom side of brick
                        self.y = brick_collider.bottom + self.radius
                return brick

    # Method for handling ball movement/acceleration
    def move_ball(self, width, height):
        # Bounce off of frame (x axis)
        if self.x < 30:
            self.dx = -self.dx
        if self.x > width - 30:
            self.dx = -self.dx

        # Bounce off of top of frame
        if self.y < 30:
            self.dy = -self.dy
        if self.y > height:
            # Lose situation
            self.state = 2

        # Multiply speed by accelaration constant (ball speed increases over time)
        if (self.speed <= 25) and self.state == 1:
            self.speed *= self.accelaration
            self.speed *= self.accelaration

        # Update ball location
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    # Method for updating collider location
    def update_collider(self):
        self.collider = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    # Method for changing/normalizing the direction variables
    def update_direction(self, dx, dy):
        # Assign new values
        self.dx = dx
        self.dy = dy

        if self.state == 1:
            # Normalizing the two variables so that their sum is equal to 1
            length = math.sqrt(self.dx**2 + self.dy**2)
            self.dx /= length
            self.dy /= length
        else:
            pass

    # Getter for ball speed
    def get_speed(self):
        return self.speed

    def get_state(self):
        return self.state

    def initialize_balls(self):
        if self.state == 0:
            self.dx = random.uniform(-1, 1)
            self.dy = random.uniform(-1, 1)
            self.state = 1
