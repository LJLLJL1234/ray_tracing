from src.ray_color import RayColor

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.default_color = RayColor(0,0,0)
        self.grid = [[self.default_color for _ in range(width)] for _ in range(height)]

    def write_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = color
        else: 
            raise IndexError("Canvas coordinates out of range")
        
    def get_pixel(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            raise IndexError("Canvas coordinates out of range")
        
    def canvas_to_ppm(self):
        header = f"P3\n{self.width} {self.height}\n255"
        body = f"joopajoo"
        return header