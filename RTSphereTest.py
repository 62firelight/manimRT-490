from manim import *

from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class RTSphereTest(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(z_range=(-4, 8, 1))
        
        labels = axes.get_axis_labels()
        
        translation = [0.25, 1.5, 1]
        x_scale = 3
        y_scale = 0.5
        z_scale = 2
        x_rotation = 75 * DEGREES
        y_rotation = 45 * DEGREES
        z_rotation = 90 * DEGREES
        
        sphere = RTSphere(translation, x_scale, y_scale, z_scale, x_rotation, y_rotation, z_rotation)
        
        red_ray = Ray3D(ORIGIN, OUT, 4, color=RED)
        
        hit_points = red_ray.get_intersection(sphere)
        
        for hit_point in hit_points:
            hit_point_obj = Dot3D(hit_point)
            self.add(hit_point_obj)
        
        y_label = MathTex("y").next_to(axes.get_y_axis().get_end(), buff=0.5)
        z_label = MathTex("z").next_to(axes.get_z_axis().get_end(), buff=0.75)
        
        ray_text = MathTex("\\text{Red Ray: }" + red_ray.get_equation())
        sphere_text = Tex("Sphere Transformations:")
        translation_text = MathTex(f"\\text{{Translated to }} {str(translation)}", font_size=39)
        scale_text = MathTex(f"\\text{{Scaled by [{x_scale}, {y_scale}, {z_scale}]}}", font_size=39)
        rotation_text = MathTex(f"\\text{{Rotated by [{x_rotation / DEGREES}, {y_rotation / DEGREES}, {z_rotation / DEGREES}]}}", font_size=39)
        
        self.set_camera_orientation(phi=60 * DEGREES, theta=-20 * DEGREES, frame_center=[0, 0, 2])
        
        top_left_group_text = VGroup(ray_text, sphere_text, translation_text, scale_text, rotation_text).arrange(DOWN, center=False, aligned_edge=LEFT).to_corner(UL)
        
        self.add(axes, sphere, red_ray)
        self.add_fixed_in_frame_mobjects(top_left_group_text)
        self.add_fixed_orientation_mobjects(y_label, z_label)
        
        