import pygame

class Board:

    surface = None
    padding = 10
    frame_color = (255, 105, 180)

    def __init__(self, surface):
        self.surface = surface 

    def render_frame(self):
        rect_left = pygame.Rect(self.padding, self.padding, 20, 720 - 2 * self.padding)
        rect_top = pygame.Rect(self.padding, self.padding, 1080 - 2 * self.padding, 20)
        rect_right = pygame.Rect(1080 - self.padding - 20, self.padding, 20, 720 - 2 * self.padding)

        pygame.draw.rect(self.surface, self.frame_color, rect_left)
        pygame.draw.rect(self.surface, self.frame_color, rect_top)
        pygame.draw.rect(self.surface, self.frame_color, rect_right)        