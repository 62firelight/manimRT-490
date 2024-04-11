from manim import *
from manim_rt import Camera
from manim_rt.FreeRay import FreeRay
from manim_rt.Ray import Ray


class RayObjectIntersectionsPoC(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi = -190 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 0.75)
        self.set_camera_orientation(phi = 45 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 1)
        
        projection_point_coords = [0, 0, 6]
        
        camera_obj = Camera.Camera(projection_point_coords, focal_length=5, width=16, height=9, total_width=5, total_height=5)
        camera = camera_obj.get_mobject()
        camera.rotate(-90 * DEGREES)
        self.add(camera)
        
        red_ray_obj = camera_obj.draw_ray(9, 5, 2, RED)
        red_ray = red_ray_obj.get_mobject()
        self.add(red_ray)
        
        blue_ray_obj = camera_obj.draw_ray(15, 2, 1)
        blue_ray = blue_ray_obj.get_mobject()
        self.add(blue_ray)
        
        # testing ray mutability
        # blue_ray_obj.set_color(RED)
        # new_ray = blue_ray_obj.change_distance(2)
        # self.add(new_ray)
        
        green_ray_obj = FreeRay(projection_point_coords, [1, 0, 0], 1.5, GREEN)
        green_ray = green_ray_obj.get_mobject()
        self.add(green_ray)
        
        sphere_along_ray = red_ray_obj.generate_sphere(1.5)
        self.add(sphere_along_ray)
        
        # self.play(GrowFromCenter(camera))
        # self.play(Create(red_ray))
        # self.play(Create(blue_ray))
        # self.play(Create(green_ray))