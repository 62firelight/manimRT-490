from manim import *

from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

import numpy as np

class TransformedRayIntersectionTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-115 * DEGREES)
        
        axes = ThreeDAxes()
        red_ray = Ray3D([-3, 0, 0], RIGHT, 10, color=RED)
        sphere = RTSphere([3.2, 1, 1], x_scale=2, y_scale=2, z_scale=2)
        sphere.set_color(BLUE)
        
        hit_points = sphere.get_intersection(red_ray)
        
        for hit_point in hit_points:
            hit_point_obj = Dot3D(hit_point)
            self.add(hit_point_obj)
        
        hit_point_normal = hit_points[0]
        green_ray = Ray3D(sphere.get_center(), hit_point_normal - sphere.get_center(), 5, color=GREEN)
        
        red_ray_equation = MathTex(red_ray.get_equation(), color=RED)
        green_ray_equation = MathTex(green_ray.get_equation(), color=GREEN)
        
        equations = VGroup(red_ray_equation, green_ray_equation).arrange(DOWN, center=False, aligned_edge=LEFT).to_corner(DL)
        
        self.add(axes, red_ray, green_ray, sphere)
        self.add_fixed_in_frame_mobjects(equations)