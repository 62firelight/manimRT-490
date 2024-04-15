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
        
        hit_point_normal = hit_points[0]
        print(hit_point_normal)
        green_ray = Ray3D(sphere.get_center(), hit_point_normal - sphere.get_center(), 3, color=GREEN)
        
        self.add(axes, red_ray, green_ray, sphere)