from __future__ import annotations
from manim import *

import numpy as np
import math

from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.RTSphere import RTSphere

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
        self.direction = normalize(direction)
        
        end = start + distance * np.array(self.direction)
        
        super().__init__(
            start=start, end=end, thickness=thickness, color=color, **kwargs
        )
        
        self.distance = distance
        
        self.homogeneous_start = np.append(start, 1)
        self.homogeneous_direction = np.append(direction, 0)
        
        self.hit_points = []
        self.normals = []
        
    def get_equation(self, homogenous_coordinates=False) -> str:
        # TODO: Round any floating point numbers 
        # TODO: Hide .0 for float numbers that are whole for consistency
        if not homogenous_coordinates:
            equation = "{} + \\lambda {}".format(np.ndarray.tolist(self.start), np.ndarray.tolist(self.direction))
        else:
            equation = "{} + \\lambda {}".format(np.ndarray.tolist(self.homogeneous_start), np.ndarray.tolist(self.homogeneous_direction))
        
        return equation
        
    def get_intersection(self, object: Mobject) -> list:        
        if type(object) == Sphere:
            translation = object.get_center()
            
            # Inverse is just the negative for translation
            # Assume spheres can only be translated for now
            inverse_translation = np.negative(translation)
            
            # apply inverse transformation
            start = np.add(self.start, inverse_translation)
            direction = self.direction
            
            a = np.dot(direction, direction)
            b = 2 * np.dot(start, direction)
            c = np.dot(start, start) - object.radius * object.radius
            
            hit_locations = self.quadratic_formula(a, b, c)
            
            hit_points = []
            normals = []
            for hit_location in hit_locations:
                hit_point = start + hit_location * np.array(direction)
                
                # apply transformation to find actual hit point
                hit_point = np.add(hit_point, translation)
                
                # for spheres, the hit point will be the normal
                # (i.e., perpendicular to the sphere)
                normals.append(hit_point)
                
                hit_points.append(hit_point)
        
            self.hit_points = hit_points
            self.normals = normals
            
            return hit_points
        elif type(object) == RTSphere:
            
            # apply inverse transformation
            start_inverse = np.matmul(object.inverse, self.homogeneous_start)
            direction_inverse = np.matmul(object.inverse, self.homogeneous_direction)
            
            inhomogeneous_start_inverse = start_inverse[:3]
            inhomogeneous_direction_inverse = direction_inverse[:3]
            
            a = np.dot(inhomogeneous_direction_inverse, inhomogeneous_direction_inverse)
            b = 2 * np.dot(inhomogeneous_start_inverse, inhomogeneous_direction_inverse)
            c = np.dot(inhomogeneous_start_inverse, inhomogeneous_start_inverse) - 1
            
            hit_locations = self.quadratic_formula(a, b, c)
            
            hit_points = []
            normals = []
            for hit_location in hit_locations:
                # find hit point for the transformed ray
                hit_point = start_inverse + hit_location * direction_inverse
                
                # apply original transformation to find actual hit point
                hit_point = np.matmul(object.transform, hit_point)
                
                hit_point = hit_point[:3]
                
                # for spheres, the hit point will be the normal
                # (i.e., perpendicular to the sphere's surface)
                normals.append(hit_point - object.get_center())
                hit_points.append(hit_point)
        
            self.hit_points = hit_points
            # TODO: Maybe give the normals to the object to keep track of?
            self.normals = normals
            
            return hit_points
        else:
            raise Exception("Unsupported object type!")
        
    def is_whole_number(self, number) -> bool:
        return number % 1 == 0
    
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
        
    def get_unit_normal(
        self,
        hit_point_number: int = 1,
        color: ParsableManimColor = WHITE
    ):
        if len(self.hit_points) <= 0 or hit_point_number < 1 or hit_point_number > len(self.hit_points):
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        index = hit_point_number - 1
        
        hit_point = self.hit_points[index]
        unit_normal = normalize(self.normals[index])
        
        unit_normal_obj = Ray3D(hit_point, unit_normal, color=color)
        
        return unit_normal_obj
    
    def get_unit_normal(
        self,
        hit_point_index: int
    ) -> Ray3D:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        unit_normal = normalize(self.normals[hit_point_index])
        
        return unit_normal
    
    def _get_unit_vector_towards_point(
        self,
        origin: np.ndarray,
        point: np.ndarray
    ):
        return normalize(point - origin)
    
    def get_light_vector(
        self,
        light_source: Mobject,
        hit_point_index: int
    ) -> Ray3D:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        hit_point = self.hit_points[hit_point_index]
        
        unit_light_vector = self._get_unit_vector_towards_point(hit_point, light_source.get_center())
        
        return unit_light_vector
    
    def get_reflected_light_vector(
        self,
        light_source: RTPointLightSource,
        hit_point_index: int
    ) -> list:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        hit_point = self.hit_points[hit_point_index]
        
        unit_normal = normalize(self.normals[hit_point_index])
        
        unit_light_vector = self._get_unit_vector_towards_point(hit_point, light_source.get_center())
        
        reflected_light_vector = 2 * np.dot(unit_normal, unit_light_vector) * unit_normal - unit_light_vector
        
        # probably unnecessary, but normalize just in case
        unit_reflected_light_vector = normalize(reflected_light_vector)
        
        return unit_reflected_light_vector
        
    # def get_viewer_vector(
    #     self,
    #     hit_point_number: int = 1,
    #     color: ParsableManimColor = WHITE
    # ) -> Ray3D:
        
    #     viewer_vector = Camera.get
        
    #     return 