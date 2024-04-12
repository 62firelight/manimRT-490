from manim import *

from manim_rt.Ray3D import Ray3D

import numpy as np

class RayIntersectionTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-115 * DEGREES)
        
        axes = ThreeDAxes()
        red_ray = Ray3D([-3, 0, 0], RIGHT, 10, color=RED)
        sphere = Sphere([3, 1, 1], radius=2)
        
        hit_points = red_ray.get_intersection(sphere)
        
        for hit_point in hit_points:
            hit_point_obj = Dot3D(hit_point)
            self.add(hit_point_obj)
        
        self.add(axes, red_ray, sphere)