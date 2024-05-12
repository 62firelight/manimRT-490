from manim import *

from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class RefractedRayTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=-135 * DEGREES, zoom=1.5)
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        sphere = RTSphere(refractive_index=1.7)
        sphere.set_color(WHITE)
        sphere.set_opacity(0.25)
        
        ray = Ray3D([-3, 3, 1], [1, -1, -0.25], 2.45, color=RED)
        
        hit_points = sphere.get_intersection(ray)
        
        refracted_ray = ray.get_refracted_ray(sphere, color=BLUE)
        print(refracted_ray.get_equation())
        
        unit_normal = Ray3D(hit_points[0], ray.get_unit_normal(0), color=GREEN)
        
        self.add(axes, labels, sphere, ray, refracted_ray, unit_normal)