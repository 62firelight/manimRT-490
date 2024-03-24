from manim import *
from manim_rt import Camera

class CustomCameraTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 45 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 1.25)
        
        focal_point_coords = [0, 0, 5]
        
        camera = Camera.drawCamera(focal_point_coords, True)
        
        # use 15 degrees for the offset
        # self.play(Rotate(camera, 385 * DEGREES, RIGHT, rate_func=linear))
        
        # self.add(camera)
        
        self.play(GrowFromCenter(camera))
        
        # TODO: generalize where these rays will go so that they always go
        # the center of each camera pixel
        ray1 = Arrow3D(focal_point_coords, [2.15, 2.15, 0], color = RED)
        ray2 = Arrow3D(focal_point_coords, [2.15, 1.25, 0], color = GREEN)
        ray3 = Arrow3D(focal_point_coords, [2.15, 0.25, 0], color = BLUE)
        
        self.play(Create(ray1))
        self.wait()
        self.play(Create(ray2))
        self.wait()
        self.play(Create(ray3))
        self.wait()