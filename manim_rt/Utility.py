import math

def solve_quadratic(
        a: float,
        b: float,
        c: float
    ) -> list:
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

def is_whole_number(
        number: float
    ) -> bool:
    return number % 1 == 0

def clamp(
        n: float,
        min: float,
        max: float
    ): 
        """
        Quick helper function for limiting numbers.
        
        source: https://www.geeksforgeeks.org/how-to-clamp-floating-numbers-in-python/ 
        """
        if n < min: 
            return min
        elif n > max: 
            return max
        else: 
            return n 