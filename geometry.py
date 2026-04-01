import math

def pythagorean_theorem(a, b):
    result = a ** 2 + b ** 2
    hypotenuse = math.sqrt(result)
    return hypotenuse

def area_of_square(a, b):
    """Calculate the area of a square.
    
    Args:
        a: Length of one side of the square
        b: Length of the other side of the square
        
    Returns:
        The area of the square
    """
    area = a * b
    return area

