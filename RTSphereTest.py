from manim import *

from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class RTSphereTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-95 * DEGREES)
        
        axes = ThreeDAxes()
        
        labels = axes.get_axis_labels()
        
        # sphere = RTSphere([2, 0, 0], 2, 0.5, 0.5, 0 * DEGREES, 0 * DEGREES, 90 * DEGREES)
        # sphere = RTSphere([0, 0, 0])
        sphere = RTSphere([0, 0, 0], 1, 1, 1, 0 * DEGREES, 0 * DEGREES, 90 * DEGREES)
        
        red_ray = Ray3D([-3, 0, 0], [1, 0, 0], 8, color=RED)
        
        hit_points = red_ray.get_intersection(sphere)
        
        for hit_point in hit_points:
            print(hit_point)
            hit_point_obj = Dot3D(hit_point)
            self.add(hit_point_obj)
        
        unit_sphere = sphere.unit_form
        
        self.add(axes, labels, sphere, red_ray)
        