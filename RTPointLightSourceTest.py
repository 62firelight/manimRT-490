from manim import *

from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class RTPointLightSourceTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-90 * DEGREES, frame_center=[0, 0, 1], zoom=1.5)
        
        axes = ThreeDAxes()
        x_label = MathTex("x").next_to(axes.get_x_axis().get_end(), buff=0.5)
        z_label = MathTex("z").next_to(axes.get_z_axis().get_end(), buff=0.5)
        
        ray = Ray3D(start=[-3, 0, 3], direction=[1, 0, -1], distance=9, color=RED)
        ray_text = MathTex("R=(-3, 0, 3) + \lambda (1, 0, -1)").next_to(ray.get_start(), OUT, buff=0.3).shift(0.5 * RIGHT)
        
        sphere = RTSphere([0, 0, -1])
        sphere.set_color(BLUE)
        
        light = RTPointLightSource(center=[3, 0, 4], color=YELLOW)
        
        ray.get_intersection(sphere)
        
        unit_normal = ray.get_unit_normal(1, GREEN)
        unit_normal_text = MathTex("\hat{n}").next_to(unit_normal.get_end(), RIGHT + OUT, buff=0.1)
        
        light_vector = ray.get_light_vector(light, 1, YELLOW)
        light_vector_text = MathTex("\hat{l}").next_to(light_vector.get_end(), RIGHT, buff=0.2)
        
        reflected_light_vector = ray.get_reflected_light_vector(light, 1, ORANGE)
        reflected_light_vector_text = MathTex("\hat{r}").next_to(reflected_light_vector.get_end(), RIGHT + OUT, buff=0.1)
        
        self.add(axes, sphere, light, ray, unit_normal, light_vector, reflected_light_vector)
        self.add_fixed_orientation_mobjects(x_label, z_label, ray_text, unit_normal_text, light_vector_text, reflected_light_vector_text)