import math

def solve_quadratic(a, b, c) -> list:
    # b^2 - 4ac
    discriminant = b * b - 4 * a * c
    
    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    elif discriminant > 0:
        x_1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b + math.sqrt(discriminant)) / (2 * a)
        
    return [x_1, x_2]

def is_whole_number(number) -> bool:
    return number % 1 == 0