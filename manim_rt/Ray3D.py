from __future__ import annotations
from math import sqrt
from manim import *

import numpy as np

from manim_rt.RTPointLightSource import RTPointLightSource

class Ray3D(Arrow3D):
    def __init__(
        self,
        start: np.ndarray = LEFT,
        direction: np.ndarray = RIGHT,
        distance: float = 1,
        intersecting_objects: np.ndarray = [],
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE,
        **kwargs,
    ) -> None:
        self.start = start
        self.direction = direction
        self.distance = distance

        self.normalized_direction = normalize(direction)
        
        self.homogeneous_start = np.append(start, 1)
        self.homogeneous_direction = np.append(direction, 0)
        
        self.hit_locations = []
        
        if len(intersecting_objects) > 0:
            for object in intersecting_objects:
                object.get_intersection(self)
                
            if len(self.hit_locations) > 0:
                print("automatic distance")
                distance = self.hit_locations[0]
        else:
            self.hit_points = []
            self.normals = []
            
        print(start, distance, self.hit_points, self.hit_locations)
        
        end = start + distance * np.array(direction)
        
        super().__init__(
            start=start, end=end, thickness=thickness, color=color, **kwargs
        )
        
        self.thickness = thickness
        self.color = color
        
    def get_equation(self, homogenous_coordinates=False) -> str:
        # TODO: Round any floating point numbers 
        # TODO: Hide .0 for float numbers that are whole for consistency
        if not homogenous_coordinates:
            equation = "{} + \\lambda {}".format(np.ndarray.tolist(self.start), np.ndarray.tolist(self.direction))
        else:
            equation = "{} + \\lambda {}".format(np.ndarray.tolist(self.homogeneous_start), np.ndarray.tolist(self.homogeneous_direction))
        
        return equation
    
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
        origin: np.ndarray | tuple[float],
        point: np.ndarray | tuple[float]
    ):
        return normalize(point - origin)
    
    def get_light_vector(
        self,
        hit_point_index: int,
        light_source: RTPointLightSource
    ) -> Ray3D:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        hit_point = self.hit_points[hit_point_index]
        
        unit_light_vector = self._get_unit_vector_towards_point(hit_point, light_source.get_center())
        
        return unit_light_vector
    
    def get_reflected_light_vector(
        self,
        hit_point_index: int,
        light_source: RTPointLightSource
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
        
    def get_viewer_vector(
        self,
        hit_point_index: int,
        camera: Mobject
    ) -> list:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        hit_point = self.hit_points[hit_point_index]
        
        unit_viewer_vector = self._get_unit_vector_towards_point(hit_point, camera.projection_point_coords)
        
        return unit_viewer_vector
    
    def get_shadow_ray(
        self,
        hit_point_index: int,
        light_source: RTPointLightSource,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE
    ) -> Ray3D:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        hit_point = self.hit_points[hit_point_index]
        
        light_vector = self.get_light_vector(hit_point_index, light_source)
        
        # calculate offset so the end of the ray is not within the light source
        offset = 0
        if type(light_source) == RTPointLightSource:
            offset = light_source.radius - offset
        
        distance_to_light_source = np.linalg.norm(hit_point - light_source.get_center()) - offset
        
        shadow_ray = Ray3D(hit_point, light_vector, distance_to_light_source, thickness, color)
        
        return shadow_ray
    
    def get_reflected_vector(
        self,
        hit_point_index: int,
        camera: Mobject
    ) -> list:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        viewer_vector = self.get_viewer_vector(hit_point_index, camera)
        
        unit_normal = self.get_unit_normal(hit_point_index)
        
        reflected_vector = 2 * np.dot(unit_normal, viewer_vector) * unit_normal - viewer_vector
        
        # probably unnecessary, but normalize just in case
        unit_reflected_vector = normalize(reflected_vector)
        
        return unit_reflected_vector
    
    def get_reflected_ray(
        self,
        hit_point_index: int,
        camera: Mobject,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE
    ) -> Ray3D:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        hit_point = self.hit_points[hit_point_index]
        
        unit_reflected_vector = self.get_reflected_vector(hit_point_index, camera)
        
        mirror_ray = Ray3D(hit_point, unit_reflected_vector, thickness=thickness, color=color)

        return mirror_ray
    
    def get_refracted_ray(
        self,
        object: Mobject,
        distance: float = 1,
        intersecting_objects: np.ndarray = [],
        refractive_index: float = 1,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE
    ) -> Ray3D:
        if len(self.hit_points) <= 0 and callable(getattr(object, "get_intersection")):
            self.hit_points = object.get_intersection(self)
        
        if len(self.hit_points) <= 0:
            # TODO: throw error
            return
        
        n1 = refractive_index
        n2 = object.refractive_index
        
        incident_ray = self.normalized_direction
        
        unit_normal = self.get_unit_normal(0)
        
        cos_angle = min(np.dot(-incident_ray, unit_normal), 1)
        
        transmitted_perpendicular = (n1 / n2) * (incident_ray + cos_angle * unit_normal)
        
        tp_mag = np.linalg.norm(transmitted_perpendicular)
        
        if tp_mag > 1:
            # simulate total internal refraction
            # i.e. n1/n2 * sin(theta) > 1
            reflected_vector = 2 * np.dot(unit_normal, -incident_ray) * unit_normal + incident_ray
            transmitted_ray = normalize(reflected_vector)
        else:
            # simulate refraction
            sin_angle = sqrt(1 - (tp_mag * tp_mag))
            transmitted_parallel = -sin_angle * unit_normal
            
            transmitted_ray =  transmitted_parallel + transmitted_perpendicular
        
        # if n1 * sin_angle > 1:
        #     reflected_vector = 2 * np.dot(unit_normal, incident_ray) * unit_normal - incident_ray
        #     transmitted_ray = normalize(reflected_vector)
        # else:
        #     transmitted_parallel = -sin_angle * unit_normal
            
        #     transmitted_ray =  transmitted_parallel + transmitted_perpendicular
        
        transmitted_ray_obj = Ray3D(self.hit_points[0], transmitted_ray, distance=distance, intersecting_objects=intersecting_objects, thickness=thickness, color=color)
        
        return transmitted_ray_obj
    
    def render_new_ray(self, distance = 1):
        return Ray3D(self.start, self.direction, distance, self.thickness, self.color)
        
        