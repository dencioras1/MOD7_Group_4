import pygame
import Brick
import random

class Board:

    bricks = [[] for _ in range(10)]

    surface = None
    padding = 10
    frame_color = (255, 105, 180)

    def __init__(self, surface):
        self.surface = surface
        self.initialize_bricks()

    def initialize_bricks(self):
        size = Brick.Brick(self.surface, 0, 0, (0, 0, 0))

        for row in range(10):
            for column in range(16):
                brick = Brick.Brick(self.surface, 20 + size.get_width() * column, 100 + size.get_height() * row, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                self.bricks[row].append(brick)

    def render_bricks(self):
        for brick_row in self.bricks:
            for brick in brick_row:
                brick.render()

    def render_frame(self):
        rect_left = pygame.Rect(0, 0, 20, 720)
        rect_top = pygame.Rect(0, 0, 1080, 20)
        rect_right = pygame.Rect(1060, 0, 20, 720)

        pygame.draw.rect(self.surface, self.frame_color, rect_left)
        pygame.draw.rect(self.surface, self.frame_color, rect_top)
        pygame.draw.rect(self.surface, self.frame_color, rect_right)        

    def remove_brick(self, brick_to_remove):
        if brick_to_remove is None:
            return
        for row in self.bricks:
            if brick_to_remove in row:
                row.remove(brick_to_remove)
                break

    def get_bricks(self):
        return [brick for row in self.bricks for brick in row]