from manim import *

from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D
from manim_rt.RTCamera import RTCamera

class RTPointLightSourceTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, frame_center=[0, 0, 1], zoom=1.5)
        
        # Axes and X + Z labels
        axes = ThreeDAxes(x_length=8)
        x_label = MathTex("x").next_to(axes.get_x_axis().get_end())
        z_label = MathTex("z").next_to(axes.get_z_axis().get_end())
        
        # Camera
        camera = RTCamera([-3, 0, 3], focal_length=1, plane_width=3, plane_height=3, total_width=1, total_height=1)
        camera.rotate(-45 * DEGREES, UP, camera.projection_point_coords)
        
        # Ray
        ray = Ray3D(start=[-3, 0, 3], direction=[1, 0, -1], distance=4.5, color=RED)
        ray_text = MathTex("R=(-3, 0, 3) + \\lambda (1, 0, -1)").next_to(ray.get_start(), OUT, buff=0.375).shift(0.5 * RIGHT)
        
        # Sphere
        sphere = RTSphere([0, 0, -1])
        sphere.set_color(BLUE)
        
        # Light Source
        light = RTPointLightSource(center=[3, 0, 4], color=YELLOW)
        
        # Calculate hit points 
        hit_points = sphere.get_intersection(ray)
        
        # First hit point
        first_hit_point = hit_points[0]
        first_hit_point_dot = Dot3D(first_hit_point, color=PURPLE)
        
        # Second hit point
        second_hit_point = hit_points[1]
        second_hit_point_dot = Dot3D(second_hit_point, color=PURPLE)
        
        # Unit normal
        unit_normal = Ray3D(first_hit_point, ray.get_unit_normal(0), color=BLUE)
        unit_normal_text = MathTex("\\hat{n}").next_to(unit_normal.get_end(), RIGHT + OUT, buff=0.1)
        
        # Light vector
        light_vector = Ray3D(first_hit_point, ray.get_light_vector(0, light), color=YELLOW)
        light_vector_text = MathTex("\\hat{l}").next_to(light_vector.get_end(), 0.1 * RIGHT + OUT, buff=0.45)
        
        # Reflected light vector
        reflected_light_vector = Ray3D(first_hit_point, ray.get_reflected_light_vector(0, light), color=ORANGE)
        reflected_light_vector_text = MathTex("\\hat{r}").next_to(reflected_light_vector.get_end(), RIGHT + OUT, buff=0.1)
        
        # Viewer vector (points towards the viewer of scene)
        viewer_vector = Ray3D(first_hit_point, ray.get_viewer_vector(0, camera), color=GREEN)
        viewer_vector_text = MathTex("\\hat{v}").next_to(viewer_vector.get_end(), IN)
        
        # Shadow ray
        shadow_ray = ray.get_shadow_ray(0, light, color=LIGHT_BROWN)
        shadow_ray_text = VGroup(Tex("\\textbf{Shadow Ray}"), Tex("(no intersections)")).arrange(DOWN, aligned_edge=LEFT).next_to(shadow_ray.get_center(), RIGHT, buff=0.001)
        
        # This sphere will intersect with the shadow ray above
        blocking_sphere = RTSphere([2, 0, 2])
        blocking_sphere.set_color(LIGHT_GRAY)
        
        # Reflected ray (assuming the sphere is reflective)
        reflected_ray = ray.get_reflected_ray(0, camera, color=GRAY)
        reflected_ray_text = MathTex("\\hat{m}").next_to(reflected_ray.get_end(), RIGHT, buff=0.1)
        
        # Add all relevants objects and text to the image
        self.add(axes, sphere, light, camera, ray, first_hit_point_dot, second_hit_point_dot, unit_normal, light_vector, reflected_light_vector, viewer_vector, shadow_ray, reflected_ray)
        self.add_fixed_orientation_mobjects(x_label, z_label, ray_text, unit_normal_text, light_vector_text, reflected_light_vector_text, viewer_vector_text, shadow_ray_text, reflected_ray_text)