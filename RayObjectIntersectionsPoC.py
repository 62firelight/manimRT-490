from manim import *
from manim_rt import Camera


class RayObjectIntersectionsPoC(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi = -190 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 0.75)
        self.set_camera_orientation(phi = 45 * DEGREES, zoom = 1)
        
        projection_point_coords = [0, 0, 2.5]
        
        camera_obj = Camera.Camera(projection_point_coords, focal_length=5, width=16, height=9, total_width=5, total_height=5)
        camera = camera_obj.get_camera()
        self.add(camera)
        
        ray = camera_obj.draw_ray(4, 6)
        self.add(ray)
        
        # ray1 = Arrow3D(projection_point_coords, camera_obj.get_grid().c2p(0.5, -1.5), color=RED)
        # self.add(ray1)
        
        # # lambda = 2
        # sphere = Sphere(radius=1, resolution=(16, 16)).shift([0.9, 0.3, -5])
        
        # # # ray direction: [0.45, 0.15, -5]
        # # ray1_start_end_coords = [0.45, 0.15, 0]
        # # ray1_start = Line3D(projection_point_coords, ray1_start_end_coords, color = RED)
        
        # # # lambda = 3
        # ray1_end_end_coords = [1.35, 0.45, -10]
        # # ray1_end = Arrow3D(ray1_start_end_coords, ray1_end_end_coords, color = RED)
        
        # # ray1 = Group(ray1_start, ray1_end)
        # ray1 = Arrow3D(projection_point_coords, ray1_end_end_coords, color=RED)
        
        # self.begin_ambient_camera_rotation(0)
        
        # self.add(ray1, sphere)
        # # self.play(Create(ray1))
        # # self.play(Create(sphere))
        
        