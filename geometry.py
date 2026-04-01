import math

def pythagorean_theorem(a, b):
    result = a ** 2 + b ** 2
    hypotenuse = math.sqrt(result)
    return hypotenuse

def rectangle_area(a, b):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    a (float): Width or length of the rectangle
    b (float): Height or breadth of the rectangle
    
    Returns:
    float: The area of the rectangle (a * b)
    """
    return a * b

