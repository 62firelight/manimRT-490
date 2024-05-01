from __future__ import annotations
from manim import *

import numpy as np

from manim_rt.RTCamera import RTCamera
from manim_rt.RTPointLightSource import RTPointLightSource

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
        self.direction = direction
        self.normalized_direction = normalize(direction)
        
        end = start + distance * np.array(direction)
        
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
        camera: RTCamera
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
        camera: RTCamera
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
        camera: RTCamera,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE
    ) -> list:
        if len(self.hit_points) <= 0 or hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            # TODO: Change this so that it throws an error and maybe break this down into separate statements
            return
        
        hit_point = self.hit_points[hit_point_index]
        
        unit_reflected_vector = self.get_reflected_vector(hit_point_index, camera)
        
        mirror_ray = Ray3D(hit_point, unit_reflected_vector, thickness=thickness, color=color)

        return mirror_ray
        