from manim import *

from manim_rt.Ray3D import Ray3D

class RayTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES, zoom=4)
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        x_ray = Ray3D(ORIGIN, [1, 0, 0], 1, color=RED)
        y_ray = Ray3D(ORIGIN, [0, 1, 0], 1, color=BLUE)
        z_ray = Ray3D(ORIGIN, [0, 0, 1], 1, color=GREEN)
        
        x_text = Tex("X", color=RED).next_to(x_ray.get_end())
        y_text = Tex("Y", color=BLUE).next_to(y_ray.get_end(), buff=0.03)
        z_text = Tex("Z", color=GREEN).next_to(z_ray.get_end(), buff=0.05)
        
        x_ray_equation = MathTex(x_ray.get_equation(), color=RED)
        y_ray_equation = MathTex(y_ray.get_equation(), color=BLUE)
        z_ray_equation = MathTex(z_ray.get_equation(), color=GREEN)
        
        equations = VGroup(x_ray_equation, y_ray_equation, z_ray_equation).arrange(DOWN).move_to([-0.25, -0.75, 0])
        
        # self.add(axes)
        # self.add(labels)
        self.add(x_ray)
        self.add(y_ray)
        self.add(z_ray)
        
        self.add_fixed_orientation_mobjects(equations)
        self.add_fixed_orientation_mobjects(x_text)
        self.add_fixed_orientation_mobjects(y_text)
        self.add_fixed_orientation_mobjects(z_text)