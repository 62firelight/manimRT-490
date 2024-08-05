from __future__ import annotations
from math import sqrt
from manim import *

import numpy as np

from manim_rt.RTPointLightSource import RTPointLightSource


class Ray3D(Arrow3D):
    """A 3D arrow representing a ray.
    
    Parameters
    ----------
    start
        The originating position of the ray.
    direction
        The direction of the ray.
    length
        The length of the ray.
    thickness
        The thickness of the ray.
    color
        The color of the ray.
    """
    def __init__(
        self,
        start: np.ndarray = LEFT,
        direction: np.ndarray = RIGHT,
        length: float = 1,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE,
        **kwargs,
    ) -> None:
        self.direction = direction
        self.normalized_direction = normalize(direction)
        
        end = start + length * np.array(direction)
        
        super().__init__(
            start=start, end=end, thickness=thickness, color=color, **kwargs
        )
        
        self.length = length
        
        self.homogeneous_start = np.append(start, 1)
        self.homogeneous_direction = np.append(direction, 0)
        
        self.hit_points = []
        self.normals = []
        
    def get_equation(
        self, 
        homogenous_coordinates=False, 
        decimal_places=1
    ) -> str:
        """Write a LaTeX equation for this ray.
        
        Parameter
        ---------
        homogeneous_coordinates
            Determine if homogeneous coordinates should be used when displaying
            the equation.
        decimal_places
            How many decimal places to round to when displaying the equation.
            
        Returns
        -------
        A string formatted as LaTeX representing the ray's equation.
        """
        if not homogenous_coordinates:
            start = self.start
            direction = self.direction
        else:
            start = self.homogeneous_start
            direction = self.homogeneous_direction
        
        # Convert to integer array if there no floats
        # Likely optional as array2string prevents trailing 
        # dots and zeros from appearing
        if all([i.is_integer() for i in start]):
            start = start.astype(int)
        if all([i.is_integer() for i in direction]):
            direction = direction.astype(int)
        
        # Formatter could be tidied up a bit
        start = np.array2string(start, separator=",", formatter={'float': lambda x: "%.0f" % x if x.is_integer() else "%.{}f".format(decimal_places) % x})
        direction = np.array2string(direction, precision=decimal_places, separator=",")
            
        equation = "{} + \\lambda {}".format(start, direction)
        
        return equation
    
    def get_unit_normal(
        self,
        hit_point_index: int
    ) -> Ray3D:
        """Gets the unit normal at a specific hit point along the ray.
        
        Parameters
        ----------
        hit_point_index
            The index number of the hit point. For example, 0 would be the
            first hit point along the ray.
            
        Returns
        -------
        A Ray3D Mobject representing the unit normal at the given hit point
        along the ray.
        """
        if len(self.hit_points) <= 0:
            raise Exception("No intersections were calculated for this ray")
        
        if hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            raise Exception("Provided hit point index was out of bounds")
        
        unit_normal = normalize(self.normals[hit_point_index])
        
        return unit_normal
    
    def _get_unit_vector_towards_point(
        self,
        origin: np.ndarray | tuple[float],
        point: np.ndarray | tuple[float]
    ):
        """Internal method for calculating unit vectors that point towards a 
        given point.
        
        Parameters
        ----------
        origin
            The starting position of the unit vector.
        point
            The location where the unit vector should point towards.
            
        Returns
        -------
        An array representing the unit vector that points towards a given
        point.
        """
        return normalize(point - origin)
    
    def get_light_vector(
        self,
        hit_point_index: int,
        light_source: RTPointLightSource
    ) -> list:
        """Calculates the "light vector," a unit vector that starts from a 
        given hit point and points towards a light source within the scene.
        
        Parameters
        ----------
        hit_point_index
            The index number of the hit point. For example, 0 would be the
            first hit point along the ray.
        light_source
            The light source mobject that the unit vector will point towards.
            
        Returns
        -------
        An array representing the light vector.
        """
        if len(self.hit_points) <= 0:
            raise Exception("No intersections were calculated for this ray")
        
        if hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            raise Exception("Provided hit point index was out of bounds")
        
        hit_point = self.hit_points[hit_point_index]
        
        unit_light_vector = self._get_unit_vector_towards_point(hit_point, light_source.get_center())
        
        return unit_light_vector
    
    def get_reflected_light_vector(
        self,
        hit_point_index: int,
        light_source: RTPointLightSource
    ) -> list:
        """Calculates the "reflected light vector," which is a light vector
        that reflects through the normal at a given hit point.
        
        Parameters
        ----------
        hit_point_index
            The index number of the hit point. For example, 0 would be the
            first hit point along the ray.
        light_source
            The light source mobject that the light vector will point towards.
            
        Returns
        -------
        An array representing the reflected light vector.
        """
        if len(self.hit_points) <= 0:
            raise Exception("No intersections were calculated for this ray")
        
        if hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            raise Exception("Provided hit point index was out of bounds")
        
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
        """Calculates the "viewer vector," a unit vector that starts from a
        given hit point and points towards the observer of a scene (i.e. a
        virtual camera)
        
        Parameters
        ----------
        hit_point_index
            The index number of the hit point. For example, 0 would be the
            first hit point along the ray.
        camera
            The virtual camera that the viewer vector will point towards.
            
        Returns
        -------
        An array representing the viewer vector.        
        """
        if len(self.hit_points) <= 0:
            raise Exception("No intersections were calculated for this ray")
        
        if hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            raise Exception("Provided hit point index was out of bounds")
        
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
        """Create a "shadow ray," a ray that starts from a given hit point and
        points towards a light source.
        
        Parameters
        ----------
        hit_point_index
            The index number of the hit point. For example, 0 would be the
            first hit point along the ray.
        light_source
            The light source Mobject that the shadow ray will point towards.
        thickness
            The thickness of the shadow ray.
        color
            The color of the shadow ray.
            
        Returns
        -------
        A Ray3D Mobject representing a shadow ray.
        """
        if len(self.hit_points) <= 0:
            raise Exception("No intersections were calculated for this ray")
        
        if hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            raise Exception("Provided hit point index was out of bounds")
        
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
        """Calculates the "reflected vector," which is the viewer vector
        reflected through the normal. 
        
        Not to be confused with the reflected light vector, which is the
        light vector reflected through the normal. 
        
        The reflected vector is used for simulating reflected surfaces in a 
        ray tracer, while the reflected light vector may be used for the 
        Phong illumination model.
        
        Parameters
        ----------
        hit_point_index
            The index number of the hit point. For example, 0 would be the
            first hit point along the ray.
        camera
            The camera mobject that the viewer vector starts from. 
            
        Returns
        -------
        An array representing the reflected vector.
        """
        if len(self.hit_points) <= 0:
            raise Exception("No intersections were calculated for this ray")
        
        if hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            raise Exception("Provided hit point index was out of bounds")
        
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
        length: float = 1,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE
    ) -> Ray3D:
        """Calculates a mobject version of the "reflected ray," which is the
        viewer vector reflected through the normal.
        
        Parameters
        ----------
        hit_point_index
            The index number of the hit point. For example, 0 would be the
            first hit point along the ray.
        camera
            The camera mobject that the viewer vector starts from. 
        length
            The length of the reflected ray.
        thickness
            The thickness of the reflected ray.
        color
            The color of the reflected ray.
            
        Returns
        -------
        A Ray3D Mobject representing the reflected vector.
        """
        if len(self.hit_points) <= 0:
            raise Exception("No intersections were calculated for this ray")
        
        if hit_point_index < 0 or hit_point_index > len(self.hit_points) - 1:
            raise Exception("Provided hit point index was out of bounds")
        
        hit_point = self.hit_points[hit_point_index]
        
        unit_reflected_vector = self.get_reflected_vector(hit_point_index, camera)
        
        mirror_ray = Ray3D(hit_point, unit_reflected_vector, length=length, thickness=thickness, color=color)

        return mirror_ray
    
    def get_refracted_ray(
        self,
        object: Mobject,
        length: float = 1,
        refractive_index: float = 1,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE
    ) -> Ray3D:
        """Calculates a "refracted ray," a ray that bends when it 
        passes over to another medium (e.g. air to water).
        
        Parameters
        ----------
        object
            The boundary between medium 1 and medium 2.
        length
            The length of the refracted ray.
        refractive_index
            The refractive index of medium 1.
        thickness
            The thickness of the refracted ray.
        color
            The color of the refracted ray.
            
        Returns
        -------
        A Ray3D Mobject representing the refracted ray.
        """
        if len(self.hit_points) <= 0 and callable(getattr(object, "get_intersection")):
            self.hit_points = object.get_intersection(self)
        
        if len(self.hit_points) <= 0:
            raise Exception("No hit points were calculated for this ray")
        
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
        
        transmitted_ray_obj = Ray3D(self.hit_points[0], transmitted_ray, length=length, thickness=thickness, color=color)
        
        return transmitted_ray_obj
        
        