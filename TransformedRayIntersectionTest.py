from manim import *

from manim_rt.RTCamera import RTCamera
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

import numpy as np

class TransformedRayIntersectionTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-90 * DEGREES)
        
        axes = ThreeDAxes()
        x_label = MathTex("x").next_to(axes.get_x_axis().get_end(), buff=0.25).shift([-0.5, 0.5, 0])
        z_label = MathTex("z").next_to(axes.get_z_axis().get_end(), buff=0.25).shift([0, 3, 0])
        red_ray = Ray3D([-4, 0, 0], RIGHT, 8, color=RED)
        camera = RTCamera([-4, 1.75, 0], image_width=3, image_height=3).rotate(90*DEGREES, RIGHT).rotate(90*DEGREES, IN)
        sphere = RTSphere([0, 0, 0], x_scale=2, y_scale=2, z_scale=2)
        sphere.set_color(BLUE)
        
        hit_points = sphere.get_intersection(red_ray)
        
        intersections_text = VGroup()
        intersections_text = VGroup(Tex("\\textbf{Hit Points}"), MathTex("(-2, 0, 0)"), MathTex("(2, 0, 0)"))
        
        for hit_point in hit_points:
            # intersections_text.add(MathTex(hit_point))
            hit_point_obj = Dot3D(hit_point)
            self.add(hit_point_obj)
            
        intersections_text.arrange(DOWN).to_corner(DR, buff=1.5).scale(1.45).shift([0, -0.35, 0])
        sphere_text = VGroup(Tex("\\textbf{Sphere at Origin}"), Tex("Radius is 2")).set_color(BLUE).arrange(DOWN).to_corner(UR, buff=1.5).scale(1.45).shift([0.25, 0.5, 0])
        # intersections_text.move_to([3, -6, 0])
        
        hit_point_normal = hit_points[0]
        
        red_ray_equation = MathTex(red_ray.get_equation(), color=RED).scale(1.25)
        
        equations = VGroup(red_ray_equation).arrange(DOWN, center=False, aligned_edge=LEFT).to_edge(LEFT).shift([0, -1.9, 0])
        
        self.add(axes, camera, red_ray, sphere)
        self.add_fixed_in_frame_mobjects(equations)
        self.add_fixed_in_frame_mobjects(intersections_text)
        self.add_fixed_in_frame_mobjects(sphere_text)
        self.add_fixed_in_frame_mobjects(x_label)
        self.add_fixed_in_frame_mobjects(z_label)