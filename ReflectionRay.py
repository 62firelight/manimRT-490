from manim import *

from manim_rt.Arc3D import Arc3D
from manim_rt.RTPlane import RTPlane
from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D
from manim_rt.RTCamera import RTCamera

class ReflectionRay(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, frame_center=[0.25, 0, 0.5], zoom=1)
        
        # Axes and X + Z labels
        axes = ThreeDAxes(x_length=8)
        
        # Camera
        camera = RTCamera([-3, 0, 3], focal_length=1, image_width=3, image_height=3, total_width=1, total_height=1)
        camera.rotate(-45 * DEGREES, UP, camera.projection_point_coords)
        
        # Ray
        ray = Ray3D(start=[-3, 0, 3], direction=[1, 0, -1], distance=5.5, thickness=0.01, color=RED)
        ray_text = MathTex("R=(-3, 0, 3) + \\lambda (1, 0, -1)").next_to(ray.get_start(), OUT, buff=0.375).shift(0.5 * RIGHT)
        
        # Sphere
        plane = RTPlane([1, 0, -1], x_scale=8, y_scale=2, opacity=0.5)
        plane.set_color(BLUE)
        
        # Calculate hit points 
        hit_points = plane.get_intersection(ray)
        
        # First hit point
        first_hit_point = hit_points[0]
        first_hit_point_dot = Dot3D(first_hit_point, radius=0.25, color=RED)
        first_hit_point_text = Tex("Hit Point").next_to(first_hit_point, direction=LEFT, buff=0.5).shift([0.25, 0, -0.55])
        
        # Unit normal
        normal = Ray3D(first_hit_point, ray.get_unit_normal(0), distance=4, color=GREEN)
        normal_text = Tex("Normal").next_to(normal.get_center(), buff=0.2).shift([0.1, 0, 1])
        
        # Mirror ray
        mirror_ray = ray.get_reflected_ray(0, camera, distance=6, color=LIGHT_GREY)
        
        # This sphere will intersect with the shadow ray above
        blocking_sphere = RTSphere([4, 0, 2], x_scale=0.5, y_scale=0.5, z_scale=0.5)
        blocking_sphere.set_color(GREEN)
        
        # Add all relevants objects and text to the image
        self.add(camera, ray, plane, first_hit_point_dot, normal, mirror_ray, blocking_sphere)
        self.add_fixed_orientation_mobjects(first_hit_point_text, normal_text)