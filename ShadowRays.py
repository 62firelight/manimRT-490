from manim import *

from manim_rt.Arc3D import Arc3D
from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D
from manim_rt.RTCamera import RTCamera

class ShadowRays(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, frame_center=[0, 0, 1.3], zoom=0.9)
        
        # Axes and X + Z labels
        axes = ThreeDAxes(x_length=8)
        x_label = MathTex("x").next_to(axes.get_x_axis().get_end())
        z_label = MathTex("z").next_to(axes.get_z_axis().get_end())
        
        # Camera
        camera = RTCamera([-3, 0, 3], focal_length=1, image_width=3, image_height=3, total_width=1, total_height=1)
        camera.rotate(-45 * DEGREES, UP, camera.projection_point_coords)
        
        # Ray
        ray = Ray3D(start=[-3, 0, 3], direction=[1, 0, -1], length=4.5, thickness=0.01, color=RED)
        ray_text = MathTex("R=(-3, 0, 3) + \\lambda (1, 0, -1)").next_to(ray.get_start(), OUT, buff=0.375).shift(0.5 * RIGHT)
        
        # Sphere
        sphere = RTSphere([0, 0, -1])
        sphere.set_color(BLUE)
        
        # Light Source 1
        light1 = RTPointLightSource(center=[-3, 0, 3], radius=0.65, color=YELLOW)
        light1_text = Tex("A").next_to(light1)
        
        # Light Source 2
        light2 = RTPointLightSource(center=[3, 0, 4], radius=0.75, color=YELLOW)
        light2_text = Tex("B").next_to(light2)
        
        # Calculate hit points 
        hit_points = sphere.get_intersection(ray)
        
        # First hit point
        first_hit_point = hit_points[0]
        first_hit_point_dot = Dot3D(first_hit_point, radius=0.25, color=RED)
        first_hit_point_text = Tex("Hit Point").next_to(first_hit_point, buff=0.65).shift([0, 0, 0.25])
        
        # Shadow ray
        shadow_ray1 = ray.get_shadow_ray(0, light1, color=LIGHT_BROWN)
        shadow_ray2 = ray.get_shadow_ray(0, light2, color=LIGHT_BROWN)
        
        # This sphere will intersect with the shadow ray above
        blocking_sphere = RTSphere([1.5, 0, 2], x_scale=0.5, y_scale=0.5, z_scale=0.5)
        blocking_sphere.set_color(GREEN)
        
        # Add all relevants objects and text to the image
        self.add(sphere, first_hit_point_dot, light1, light2, shadow_ray1, shadow_ray2, blocking_sphere)
        self.add_fixed_orientation_mobjects(first_hit_point_text, light1_text, light2_text)