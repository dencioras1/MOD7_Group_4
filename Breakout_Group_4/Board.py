import pygame
import Brick
import random

class Board:

    # Board class attributes

    bricks = [[] for _ in range(10)]
    surface = None
    padding = 10
    frame_color = (255, 105, 180)

    # Constructor
    def __init__(self, surface):
        # Surface of board
        self.surface = surface
        self.initialize_bricks()

    # Method for generating the bricks
    def initialize_bricks(self):
        # Empty brick object for retrieving the size variables
        size = Brick.Brick(0, 0, (0, 0, 0))

        # For each row (10 in total)
        for row in range(10):
            # For eache collumn (16 in total)
            for column in range(16):
                # Create new brick with randomized RGB values and add it to the 2D array of bricks
                brick = Brick.Brick(20 + size.get_width() * column, 100 + size.get_height() * row, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                self.bricks[row].append(brick)

    # Method for drawing the bricks
    def draw_bricks(self):
        # For each row of bricks in the 2D array...
        for brick_row in self.bricks:
            # For each brick in the brick row...
            for brick in brick_row:
                # Draw the brick
                brick.draw_brick(self.surface)

    # Method for drawing the board frame
    def draw_frame(self):
        # Rect variables
        rect_left = pygame.Rect(0, 0, 20, 720)
        rect_top = pygame.Rect(0, 0, 1080, 20)
        rect_right = pygame.Rect(1060, 0, 20, 720)

        # Draw rects
        pygame.draw.rect(self.surface, self.frame_color, rect_left)
        pygame.draw.rect(self.surface, self.frame_color, rect_top)
        pygame.draw.rect(self.surface, self.frame_color, rect_right)        

    # Method for removing a brick
    def remove_brick(self, brick_to_remove):
        # Go throug each 2D array row
        for row in self.bricks:
            # If the brick_to_remove is in the row, remove it
            if brick_to_remove in row:
                row.remove(brick_to_remove)
                break
    
    # Getter for the 2D array of bricks
    def get_bricks(self):
        return [brick for row in self.bricks for brick in row]