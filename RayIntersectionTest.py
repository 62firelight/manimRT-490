from manim import *

from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

import numpy as np

class RayIntersectionTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-95 * DEGREES)
        
        axes = ThreeDAxes()
        red_ray = Ray3D([-3, 0, 0], RIGHT, 5, color=RED)
        # green_ray = Ray3D([-3, 0, 3], [3, 0, -3], 2, color=GREEN)
        sphere = RTSphere()
        
        hit_points = sphere.get_intersection(red_ray)
        
        for hit_point in hit_points:
            hit_point_obj = Dot3D(hit_point)
            self.add(hit_point_obj)
            # self.add_fixed_in_frame_mobjects(Text(str(np.ndarray.tolist(hit_point)), font_size=22, color=YELLOW).next_to(hit_point_obj, DOWN))
        
        self.add(axes, red_ray, sphere)