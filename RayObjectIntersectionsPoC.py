from manim import *
from manim_rt import Camera


class RayObjectIntersectionsPoC(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = -190 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 0.75)
        
        focal_point_coords = [0, 0, 5]
        
        camera = Camera.drawCamera(focal_point_coords)
        self.add(camera)
        
        # lambda = 2
        sphere = Sphere(radius=1, resolution=(16, 16)).shift([0.9, 0.3, -5])
        
        # # ray direction: [0.45, 0.15, -5]
        # ray1_start_end_coords = [0.45, 0.15, 0]
        # ray1_start = Line3D(focal_point_coords, ray1_start_end_coords, color = RED)
        
        # # lambda = 3
        ray1_end_end_coords = [1.35, 0.45, -10]
        # ray1_end = Arrow3D(ray1_start_end_coords, ray1_end_end_coords, color = RED)
        
        # ray1 = Group(ray1_start, ray1_end)
        ray1 = Arrow3D(focal_point_coords, ray1_end_end_coords, color=RED)
        
        self.begin_ambient_camera_rotation(0)
        
        # self.add(sphere)
        self.play(Create(ray1))
        self.play(Create(sphere))
        
        