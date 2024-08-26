from src.ray_color import RayColor

def add_colors(color1, color2):
    return RayColor(color1.r + color2.r, color1.g + color2.g, color1.b + color2.b)

def subtract_colors(color1, color2):
    return RayColor(color1.r - color2.r, color1.g - color2.g, color1.b - color2.b)

def multiply_color(color1, color2):
    if isinstance(color2, RayColor):
        return RayColor(color1.r * color2.r, color1.g * color2.g, color1.b * color2.b)
        
    else:
        scalar = color2
        return RayColor(color1.r * scalar, color1.g * scalar, color1.b * scalar)