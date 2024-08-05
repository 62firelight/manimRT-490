from manim import *

from manim_rt.Arc3D import Arc3D
from manim_rt.RTPlane import RTPlane
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class TotalInternalRefractionTest(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=85 * DEGREES, theta=-180 * DEGREES, zoom=1.75)
        self.set_camera_orientation(phi=85 * DEGREES, theta=-90 * DEGREES, zoom=1.75)
        
        # Axes for easier placement of objects
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        # Planes
        bottom_air_plane = RTPlane(x_scale=8, refractive_index=1)
        top_air_plane = RTPlane(translation=[0, 0, 0.5], x_scale=8, refractive_index=1)
        
        # Incident ray
        ray_start = [-2, 0, 0.5]
        ray = Ray3D(ray_start, np.subtract([-1, 0, 0], ray_start), 1, color=RED)
        
        # Objects
        self.add(bottom_air_plane, top_air_plane, ray)
        
        # Text
        n1_text = MathTex("n_1 = 1.33").next_to(ray.get_center(), LEFT)
        
        n2_top_text = MathTex("n_2 = 1").next_to(ORIGIN, OUT, 1)
        n2_bottom_text = MathTex("n_2 = 1").next_to(ORIGIN, IN, 0.5)
        
        self.add_fixed_orientation_mobjects(n1_text, n2_top_text, n2_bottom_text)
        
        for i in range(6):
            if i % 2 == 0:
                intersecting_plane = bottom_air_plane
                ray_color = GREEN
            else:
                intersecting_plane = top_air_plane
                ray_color = RED
            
            # Calculate intersection so we can actually get the refracted ray
            intersecting_plane.get_intersection(ray)
            
            # First (of many) refracted rays that get reflected instead due to Total Internal Reflection
            refracted_ray = ray.get_refracted_ray(bottom_air_plane, color=ray_color, length=1.125, refractive_index=1.33)
            
            self.add(refracted_ray)
            
            ray = refracted_ray