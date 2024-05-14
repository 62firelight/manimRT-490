from manim import *

from manim_rt.Arc3D import Arc3D
from manim_rt.RTPlane import RTPlane
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class RefractedRayTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=89 * DEGREES, theta=-180 * DEGREES, zoom=1.75)
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        plane = RTPlane()
        
        ray_start = [-1, 1, 0.5]
        ray = Ray3D(ray_start, ORIGIN - ray_start, 1, color=RED)
        
        hit_points = plane.get_intersection(ray)
        
        unit_normal_n1 = Ray3D(hit_points[0], ray.get_unit_normal(0), color=GREEN)
        
        angle_n1 = Arc3D(ray, unit_normal_n1)
        angle_n1_text = MathTex("\\theta_1").next_to(angle_n1.get_center() + 0.1 * UP, OUT)
        
        unit_normal_n2 = Ray3D(hit_points[0], [0, 0, -1], color=ORANGE)
        
        refracted_ray = ray.get_refracted_ray(plane, color=BLUE)
        
        angle_n2 = Arc3D(refracted_ray, unit_normal_n2)
        angle_n2_text = MathTex("\\theta_2").next_to(angle_n2.get_center() + 0.2 * DOWN, IN)
        
        n1_text = MathTex("n_1 = 1").next_to(unit_normal_n1.get_end() + 0.375 * OUT + 0.05 * DOWN, DOWN)
        n2_text = MathTex("n_2 = 1.33").next_to(unit_normal_n2.get_end() + 0.375 * IN + 0.25 * DOWN, DOWN)
        
        self.add(plane, ray, refracted_ray, unit_normal_n1, unit_normal_n2, angle_n1, angle_n2)
        
        self.add_fixed_orientation_mobjects(angle_n1_text, angle_n2_text, n1_text, n2_text)