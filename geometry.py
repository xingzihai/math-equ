import math

def pythagorean_theorem(a, b):
    result = a ** 2 + b ** 2
    hypotenuse = math.sqrt(result)
    return hypotenuse

def area_of_triangle(base, height):
    """Calculate the area of a triangle.
    
    Args:
        base: Length of the base of the triangle
        height: Height of the triangle
        
    Returns:
        The area of the triangle
    """
    area = base * height / 2
    return area