from manim import *
from manim_rt import Camera
from manim_rt.FreeRay import FreeRay
from manim_rt.Ray import Ray


class RayObjectIntersectionsSketch(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi = -190 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 0.75)
        self.set_camera_orientation(phi = 52 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 1)
        
        projection_point_coords = [0, 0, 6]
        
        camera_obj = Camera.Camera(projection_point_coords, focal_length=5, width=16, height=9, total_width=5, total_height=5)
        camera = camera_obj.get_mobject()
        camera.rotate(-90 * DEGREES)
        
        red_ray_obj = camera_obj.draw_ray(9, 5, 3, RED)
        red_ray = red_ray_obj.get_mobject()
        
        blue_ray_obj = camera_obj.draw_ray(15, 8, 1.75)
        blue_ray = blue_ray_obj.get_mobject()
        
        sphere_along_ray = red_ray_obj.generate_sphere(2.5)
        sphere_along_ray.set_color(GREEN)
        
        camera_text = Text("Camera").shift(LEFT * 3, DOWN * 3)
        sphere_text = Text("Sphere").shift(RIGHT * 4.5, DOWN * 1.15)
        
        red_ray_text = Text("Red ray intersects", color=RED, font_size=36).shift(RIGHT * 3, DOWN * 0.85)
        
        blue_ray_text = Text("Blue ray does not intersect", color=BLUE, font_size=36).shift(RIGHT * 3.95, DOWN * 1.575)
        
        # self.add(camera)
        # self.add(sphere_along_ray)
        # self.add(red_ray)
        # self.add(blue_ray)
        
        # self.clear()
        self.play(GrowFromCenter(camera, run_time=2))
        
        self.add_fixed_in_frame_mobjects(camera_text)
        self.play(FadeIn(camera_text))
        
        self.play(GrowFromCenter(sphere_along_ray, run_time=2))
        
        self.add_fixed_in_frame_mobjects(sphere_text)
        self.play(FadeIn(sphere_text))
        
        self.wait(1)
        self.play(FadeOut(camera_text, sphere_text))
        
        self.play(Create(red_ray, run_time=2))
        
        self.add_fixed_in_frame_mobjects(red_ray_text)
        self.play(FadeIn(red_ray_text))
        
        self.play(Create(blue_ray, run_time=2))
        
        self.add_fixed_in_frame_mobjects(blue_ray_text)
        self.play(FadeIn(blue_ray_text))
        
        self.wait(1)