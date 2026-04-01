import math

def pythagorean_theorem(a, b):
    result = a ** 2 + b ** 2
    hypotenuse = math.sqrt(result)
    return hypotenuse

def area_of_trapezoid(first_base, second_base, height):
    """Calculate the area of a trapezoid.
    
    Args:
        first_base: Length of the first parallel side
        second_base: Length of the second parallel side
        height: Height of the trapezoid
        
    Returns:
        The area of the trapezoid
    """
    area = (first_base + second_base) * height / 2
    return area

