import math

"""
Utility.py

A file for storing utility functions that may be useful across a variety of 
situations.
"""

def solve_quadratic(
        a: float,
        b: float,
        c: float
    ) -> list:
    """Solves a quadratic equation that is set equal to 0.
    
    Args:
        a: The a value to substitute into the quadratic formula.
        b: The b value to substitute into the quadratic formula.
        c: The c value to substitute into the quadratic formula.
        
    Returns:
        An array containing the solution(s) to the given quadratic equation.
    This array will be empty if there are no solutions.
    """
    
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
    """Check if a given number is considered to be an integer.
    
    Args:
        number: The number to check.
        
    Returns:
        A boolean determining whether the given number is an integer or not.
    """
    return number % 1 == 0

def clamp(
        n: float,
        min: float,
        max: float
    ): 
        """
        Quick helper function for limiting numbers.
        
        source: https://www.geeksforgeeks.org/how-to-clamp-floating-numbers-in-python/ 
        
        Args:
            n: The number to limit.
            min: The lower bound of the number.
            max: The upper bound of the number.
            
        Returns:
            A number that falls in the domain [min, max].
        """
        if n < min: 
            return min
        elif n > max: 
            return max
        else: 
            return n 