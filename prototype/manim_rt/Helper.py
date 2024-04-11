def clamp(n, min, max): 
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
