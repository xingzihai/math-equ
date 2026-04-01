import math

def pythagorean_theorem(a, b):
    result = a ** 2 + b ** 2
    hypotenuse = math.sqrt(result)
    return hypotenuse

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

