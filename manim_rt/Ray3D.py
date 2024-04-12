from manim import *

import numpy as np
import math

class Ray3D(Arrow3D):
    def __init__(
        self,
        start: np.ndarray = LEFT,
        direction: np.ndarray = RIGHT,
        distance: float = 1,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE,
        **kwargs,
    ) -> None:
        # TODO: Normalize the direction
        self.direction = direction
        
        end = start + distance * np.array(self.direction)
        
        super().__init__(
            start=start, end=end, thickness=thickness, color=color, **kwargs
        )
        
        self.distance = distance
        
    def get_intersection(self, sphere: Sphere) -> list:        
        # a = d dot d
        # b = 2(p_0 dot d)
        # c = p_0 dot p_0 - r^2
        
        a = np.dot(self.direction, self.direction)
        b = 2 * np.dot(self.start, self.direction)
        c = np.dot(self.start, self.start) - sphere.radius * sphere.radius
        
        hit_locations = self.quadratic_formula(a, b, c)
        
        hit_points = []
        for hit_location in hit_locations:
            hit_point = self.start + hit_location * np.array(self.direction)
            # hit_point_obj = Dot3D(hit_point, color=color)
            hit_points.append(hit_point)
        
        return hit_points
    
    def quadratic_formula(self, a, b, c) -> list:
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