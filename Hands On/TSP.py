import numpy as np
import pygame
from support_functions import TSPDecoder


class TSP:

    rows = 40
    columns = 2
    TSP = TSPDecoder(rows=rows, columns=columns)
    grid = np.zeros((rows, columns), dtype=int)

    def __init__(self):
        self.rows = TSP.rows
        self.columns = TSP.columns
        self.grid = np.zeros((self.rows, self.columns), dtype=int)

    def TSP_update(self):
        for row in range(2):
            for column in range(40):
                pass





