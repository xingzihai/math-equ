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
  
def area_of_rectangle(a, b):
    """Calculate the area of a rectangle.
    
    Args:
        a: Length of one side of the rectangle
        b: Length of the other side of the rectangle
        
    Returns:
        The area of the rectangle
    """
    area = a * b
    return area
  
  

