from manim import *

from manim_rt.Arc3D import Arc3D
from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D
from manim_rt.RTCamera import RTCamera

class RTPointLightSourceTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, theta=-95 * DEGREES, frame_center=[0, 0, 0.65], zoom=5)
        
        phong = MathTex("I(\\boldsymbol{p})=I_ak_a + I_dk_d(",
                        "\\boldsymbol{\hat{n}}",
                        "\cdot", 
                        "\\boldsymbol{\hat{l}}", 
                        ") + I_sk_s(", 
                        "\\boldsymbol{\hat{r}}", 
                        "\cdot", 
                        "\\boldsymbol{\hat{v}}", 
                        ")^a")
        
        phong.set_color_by_tex("\\boldsymbol{\hat{n}}", BLUE)
        phong.set_color_by_tex("\\boldsymbol{\hat{l}}", YELLOW)
        phong.set_color_by_tex("\\boldsymbol{\hat{r}}", ORANGE)
        phong.set_color_by_tex("\\boldsymbol{\hat{v}}", GREEN)
        
        phong.scale(1.45)
        
        phong.move_to([0.125, 0, 1.25])
        
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
        
        # Light Source
        light = RTPointLightSource(center=[3, 0, 4], radius=0.1, color=YELLOW)
        
        # Calculate hit points 
        hit_points = sphere.get_intersection(ray)
        
        # First hit point
        first_hit_point = hit_points[0]
        first_hit_point_dot = Dot3D(first_hit_point, color=LIGHT_PINK)
        
        # Second hit point
        second_hit_point = hit_points[1]
        second_hit_point_dot = Dot3D(second_hit_point, color=PURPLE)
        
        # Unit normal
        unit_normal = Ray3D(first_hit_point, ray.get_unit_normal(0), color=BLUE)
        unit_normal_text = MathTex("\\boldsymbol{\\hat{n}}", color=BLUE).scale(2).next_to(unit_normal.get_end(), RIGHT, buff=-0.1)
        
        # Light vector
        light_vector = Ray3D(first_hit_point, ray.get_light_vector(0, light), color=YELLOW)
        light_vector_text = MathTex("\\boldsymbol{\\hat{l}}", color=YELLOW).scale(2).next_to(light_vector.get_end(), RIGHT, buff=0.1)
        
        # Reflected light vector
        reflected_light_vector = Ray3D(first_hit_point, ray.get_reflected_light_vector(0, light), color=ORANGE)
        reflected_light_vector_text = MathTex("\\boldsymbol{\\hat{r}}", color=ORANGE).scale(2).next_to(reflected_light_vector.get_end(), RIGHT + OUT, buff=0.01)
        
        # Viewer vector (points towards the viewer of scene)
        viewer_vector = Ray3D(first_hit_point, ray.get_viewer_vector(0, camera), color=GREEN)
        viewer_vector_text = MathTex("\\boldsymbol{\\hat{v}}", color=GREEN).scale(2).next_to(viewer_vector.get_end(), IN)
        
        # Shadow ray
        shadow_ray = ray.get_shadow_ray(0, light, color=LIGHT_BROWN)
        shadow_ray_text = VGroup(Tex("\\textbf{Shadow Ray}"), Tex("(no intersections)")).arrange(DOWN, aligned_edge=LEFT).next_to(shadow_ray.get_center(), RIGHT, buff=0.001)
        
        # This sphere will intersect with the shadow ray above
        blocking_sphere = RTSphere([2, 0, 2])
        blocking_sphere.set_color(LIGHT_GRAY)
        
        # Reflected ray (assuming the sphere is reflective)
        reflected_ray = ray.get_reflected_ray(0, camera, color=GRAY)
        reflected_ray_text = MathTex("\\hat{m}").next_to(reflected_ray.get_end(), RIGHT, buff=0.1)
        
        angle_between_normal_and_light = Arc3D(unit_normal, light_vector)
        angle_between_reflected_and_viewer = Arc3D(reflected_light_vector, viewer_vector)
        
        # Add all relevant objects and text to the image
        # self.add(sphere)
        # self.add(light)
        # self.add(camera)
        # self.add(ray)
        # self.add(first_hit_point_dot)
        # self.add(second_hit_point_dot) 
        # self.add(unit_normal) 
        # self.add(light_vector) 
        # self.add(reflected_light_vector)
        # self.add(viewer_vector)
        # self.add(angle_between_normal_and_light)
        # self.add(angle_between_reflected_and_viewer)
        
        # self.add_fixed_orientation_mobjects(x_label)
        # self.add_fixed_orientation_mobjects(z_label)
        # self.add_fixed_orientation_mobjects(ray_text)
        self.add_fixed_orientation_mobjects(phong)
        self.add_fixed_orientation_mobjects(unit_normal_text)
        self.add_fixed_orientation_mobjects(light_vector_text)
        self.add_fixed_orientation_mobjects(reflected_light_vector_text)
        self.add_fixed_orientation_mobjects(viewer_vector_text)
        
        self.begin_ambient_camera_rotation(0) # to properly show intersections
        
        # ensure text displays properly
        phong.set_color_by_tex("\\boldsymbol{\hat{n}}", BLACK)
        phong.set_color_by_tex("\\boldsymbol{\hat{l}}", BLACK)
        phong.set_color_by_tex("\\boldsymbol{\hat{r}}", BLACK)
        phong.set_color_by_tex("\\boldsymbol{\hat{v}}", BLACK)
        
        self.remove(phong)
        self.remove(unit_normal_text)
        self.remove(light_vector_text)
        self.remove(reflected_light_vector_text)
        self.remove(viewer_vector_text)
        
        self.play(GrowFromCenter(sphere))
        self.play(GrowFromCenter(light))
        self.play(Create(ray, run_time=1.5))
        self.play(GrowFromCenter(first_hit_point_dot))
        self.play(Write(phong))
        self.play(Create(unit_normal, run_time=1.5))
        phong.set_color_by_tex("\\boldsymbol{\hat{n}}", BLUE)
        self.play(FadeIn(unit_normal_text))
        self.play(Create(light_vector, run_time=1.5))
        phong.set_color_by_tex("\\boldsymbol{\hat{l}}", YELLOW)
        self.play(FadeIn(light_vector_text))
        self.play(Create(reflected_light_vector, run_time=1.5))
        phong.set_color_by_tex("\\boldsymbol{\hat{r}}", ORANGE)
        self.play(FadeIn(reflected_light_vector_text))
        self.play(Create(viewer_vector, run_time=1.5))
        phong.set_color_by_tex("\\boldsymbol{\hat{v}}", GREEN)
        self.play(FadeIn(viewer_vector_text))
        self.play(Create(angle_between_normal_and_light))
        self.play(Create(angle_between_reflected_and_viewer))
        self.wait(1)