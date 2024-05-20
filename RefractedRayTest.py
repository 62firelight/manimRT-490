from manim import *

from manim_rt.Arc3D import Arc3D
from manim_rt.RTPlane import RTPlane
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class RefractedRayTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=89 * DEGREES, theta=-180 * DEGREES, zoom=1.75)
        
        # Axes for easier placement of objects
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        # Planes (maybe the air plane should be a different colour)
        water_plane = RTPlane(refractive_index=1.33)
        air_plane = RTPlane([0, -1, -1], refractive_index=1)
        
        # Incident ray
        ray_start = [-1, 1, 0.5]
        ray = Ray3D(ray_start, ORIGIN - ray_start, 1, color=RED)
        
        # Calculate intersection so we can actually get the refracted ray
        hit_points = water_plane.get_intersection(ray)
        
        # Unit normal for n1
        unit_normal_n1 = Ray3D(hit_points[0], ray.get_unit_normal(0), color=GREEN)
        
        # Angle between unit normal for n1 and incident ray
        angle_n1 = Arc3D(ray, unit_normal_n1)
        angle_n1_text = MathTex("\\theta_1").next_to(angle_n1.get_center() + 0.1 * UP, OUT)
        
        # Unit normal for n2
        unit_normal_n2 = Ray3D(hit_points[0], [0, 0, -1], color=ORANGE)
        
        # Our first refracted ray travelling from air into water
        first_refracted_ray = ray.get_refracted_ray(water_plane, color=BLUE, distance=1.5)
        
        # Angle between unit normal for n2 and the first refracted ray
        angle_n2 = Arc3D(unit_normal_n2, first_refracted_ray)
        angle_n2_text = MathTex("\\theta_2").next_to(angle_n2.get_center() + 0.2 * DOWN, IN)
        
        # Show refractive indices
        n1_text = MathTex("n = 1").next_to(unit_normal_n1.get_center(), DOWN, buff=0.35)
        n2_text = MathTex("n = 1.33").next_to(first_refracted_ray.get_center(), DOWN, buff=0.75)
        
        # Calculate intersection for refracted ray so we can show the second refracted ray
        refracted_ray_hit_points = air_plane.get_intersection(first_refracted_ray)
        
        # Our second refracted ray travelling from water to air
        # The direction of this ray should be the same as the previous incident ray
        second_refracted_ray = first_refracted_ray.get_refracted_ray(air_plane, refractive_index=1.33, distance=2, color=RED)
        
        # Show last refractive index 
        n3_text = MathTex("n = 1").next_to(second_refracted_ray.get_center(), IN, buff=0.5)
        
        # Objects
        self.add(axes, labels, water_plane, air_plane, ray, first_refracted_ray, unit_normal_n1, unit_normal_n2, angle_n1, angle_n2, second_refracted_ray)
        
        # Text
        self.add_fixed_orientation_mobjects(angle_n1_text, angle_n2_text, n1_text, n2_text, n3_text)