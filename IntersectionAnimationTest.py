from manim import *

from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D


class IntersectionAnimationTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=90 * DEGREES, frame_center=[1.75, 0, 2], zoom=1.5)
        
        axes = ThreeDAxes()
        
        x_label = MathTex("x").next_to(axes.get_x_axis().get_end(), buff=0.25)
        z_label = MathTex("z").next_to(axes.get_z_axis().get_end(), buff=0.25)
        
        ray = Ray3D(ORIGIN, [1, 0, 1], 7, color=RED)
        
        sphere = RTSphere([4, 0, 3])
        
        hit_points = sphere.get_intersection(ray)
        
        self.add(axes, sphere)
        # self.add(ray)
        # for hit_point in hit_points:
        #     self.add(Dot3D(hit_point, color=YELLOW, radius=0.12))
        self.add_fixed_orientation_mobjects(x_label, z_label)
        
        # Animation begins here
        self.play(Create(ray))
        for hit_point in hit_points:
            self.play(GrowFromCenter(Dot3D(hit_point, color=YELLOW, radius=0.12)))
        self.wait()