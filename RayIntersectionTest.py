from manim import *

from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D


class RayIntersectionTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-95 * DEGREES)
        axes = ThreeDAxes()
        red_ray = Ray3D([-3, 0, 0], RIGHT, 5, color=RED)
        sphere = RTSphere(color=BLUE)
        hit_points = sphere.get_intersection(red_ray)
        for hit_point in hit_points:
            hit_point_obj = Dot3D(hit_point)
            self.add(hit_point_obj)
        self.add(axes, red_ray, sphere)