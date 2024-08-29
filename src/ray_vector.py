import numpy as np

class RayVector:
    def __init__(self, xyzp):
        self._coords = np.array(xyzp)

    @property
    def coords(self):
        return self._coords
    
    def x(self):
        return self.coords[0]

    def y(self):
        return self.coords[1]
    
    def z(self):
        return self.coords[2]

    def _is_point(self):
        return self.coords[3] == 1
    
    def _is_vector(self):
        return self.coords[3] == 0

    def __add__(self, other):
        if not isinstance(other, RayVector):
            return NotImplemented
        result_coords = self.coords + other.coords
        return RayVector(result_coords)
    
    def __sub__(self, other):
        if not isinstance(other, RayVector):
            return NotImplemented
        result_coords = self.coords - other.coords
        return RayVector(result_coords)
    
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        result_coords = self.coords * other
        return RayVector(result_coords)
    
    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ValueError("Cannot divide by zero")
        result_coords = self.coords / other
        return RayVector(result_coords)

    def magnitude(self):
        return np.linalg.norm(self.coords)
    
    def normalize(self):
        return self / self.magnitude()