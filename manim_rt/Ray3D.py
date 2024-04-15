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
        
        self.homogenous_start = np.append(start, 1)
        self.homogenous_direction = np.append(direction, 0)
        
    def get_intersection(self, object: Mobject) -> list:        
        if type(object) == Sphere:
            translation = object.get_center()
            
            # Inverse is just the negative for translation
            # Assume spheres can only be translated for now
            inverse_translation = np.negative(translation)
            
            start = np.add(self.start, inverse_translation)
            direction = self.direction
            
            a = np.dot(direction, direction)
            b = 2 * np.dot(start, direction)
            c = np.dot(start, start) - object.radius * object.radius
            
            hit_locations = self.quadratic_formula(a, b, c)
            
            hit_points = []
            for hit_location in hit_locations:
                hit_point = start + hit_location * np.array(direction)
                hit_point = np.add(hit_point, translation)
                hit_points.append(hit_point)
        
            return hit_points
        else:
            raise Exception("Unsupported object type!")
    
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