import numpy as np
from math import ceil

class RayColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"RayColor(r={self.r}, g={self.g}, b={self.b})"
    
    def __eq__(self, other):
        if isinstance(other, RayColor):
            return self.r == other.r and self.g == other.g and self.b == other.b
        return False
    
    def get_colors(self):
        return [self.r, self.g, self.b]
    
    def get_scaled_colors(self):
        colors = self.get_colors()
        scaled_colors = []
        for c in colors:
            scaled_c = ceil(max(0, min(c, 1)) * 255)
            scaled_colors.append(scaled_c)
        return scaled_colors


        
