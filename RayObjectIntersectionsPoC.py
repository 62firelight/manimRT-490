from manim import *
from manim_rt import Camera


class RayObjectIntersectionsPoC(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi = -190 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 0.75)
        self.set_camera_orientation(phi = 75 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 1)
        
        projection_point_coords = [0, 0, 2.5]
        
        camera_obj = Camera.Camera(projection_point_coords, focal_length=5, width=16, height=9, total_width=5, total_height=5)
        camera = camera_obj.get_camera()
        self.add(camera)
        
        ray_obj = camera_obj.draw_ray(8, 5, 1)
        ray = ray_obj.get_mobject()
        self.add(ray)
        ray_obj.set_color(RED)
        new_ray = ray_obj.change_distance(2)
        self.add(new_ray)