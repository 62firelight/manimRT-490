from manim import *

from manim_rt.Arc3D import Arc3D
from manim_rt.RTPlane import RTPlane
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class TotalInternalRefractionTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-180 * DEGREES, zoom=1.75, frame_center=[0, 0, 0.25])
        
        # Axes for easier placement of objects
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        # Planes
        bottom_air_plane = RTPlane(y_scale=4, refractive_index=1)
        top_air_plane = RTPlane(translation=[0, 0, 0.5], y_scale=4, refractive_index=1)
        
        # Incident ray
        ray_start = [-1, 2.5, 0.5]
        ray = Ray3D(ray_start, np.subtract([0, 1.5, 0], ray_start), intersecting_objects=[bottom_air_plane], color=RED)
        
        # Calculate intersection so we can actually get the refracted ray
        # bottom_air_plane.get_intersection(ray)
        
        # First (of many) refracted rays that get reflected instead due to Total Internal Reflection
        refracted_ray = ray.get_refracted_ray(bottom_air_plane, color=GREEN, intersecting_objects=[top_air_plane], refractive_index=1.33)
        
        self.add(refracted_ray)
        
        # Calculate more refracted rays!
        
        for i in range(6):
            if i % 2 == 0:
                ray_color = RED
                # top_air_plane.get_intersection(refracted_ray)
                refracted_ray = refracted_ray.get_refracted_ray(top_air_plane, color=ray_color, intersecting_objects=[bottom_air_plane], refractive_index=1.33)
            else:
                ray_color = GREEN
                # bottom_air_plane.get_intersection(refracted_ray)
                refracted_ray = refracted_ray.get_refracted_ray(bottom_air_plane, color=ray_color, intersecting_objects=[top_air_plane], refractive_index=1.33)
            self.add(refracted_ray)
        
        # top_air_plane.get_intersection(first_refracted_ray)
        
        # second_refracted_ray = first_refracted_ray.get_refracted_ray(top_air_plane, color=RED, distance=1.5, refractive_index=1.33)
        
        # bottom_air_plane.get_intersection(second_refracted_ray)
        
        # third_refracted_ray = second_refracted_ray.get_refracted_ray(bottom_air_plane, color=GREEN, distance=1.5, refractive_index=1.33)
        
        # top_air_plane.get_intersection(third_refracted_ray)
        
        # fourth_refracted_ray = third_refracted_ray.get_refracted_ray(top_air_plane, color=RED, distance=1.8, refractive_index=1.33)
        
        # bottom_air_plane.get_intersection(fourth_refracted_ray)
        
        # fifth_refracted_ray = fourth_refracted_ray.get_refracted_ray(bottom_air_plane, color=GREEN, distance=1.5, refractive_index=1.33)
        
        # top_air_plane.get_intersection(fifth_refracted_ray)
        
        # sixth_refracted_ray = fifth_refracted_ray.get_refracted_ray(top_air_plane, color=RED, distance=1.9, refractive_index=1.33)
        
        # Objects
        self.add(bottom_air_plane, top_air_plane, ray)
        
        # Text
        n1_text = MathTex("n_1 = 1.33").next_to(ray.get_center(), UP, 1.05)
        
        n2_top_text = MathTex("n_2 = 1").next_to(ORIGIN, OUT, 1)
        n2_bottom_text = MathTex("n_2 = 1").next_to(ORIGIN, IN, 0.5)
        
        self.add_fixed_orientation_mobjects(n1_text, n2_top_text, n2_bottom_text)