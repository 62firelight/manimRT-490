from manim import * 
from manim_rt import *
from manim_rt.RTCamera import RTCamera
from manim_rt.Ray3D import Ray3D
 

class CameraTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=-45*DEGREES)
        # self.set_camera_orientation(phi = 55 * DEGREES, theta = -90 * DEGREES, gamma = 90 * DEGREES, zoom = 1.25)
        
        camera = RTCamera([0, 0, 4], focal_length=5)
        # camera.rotate(-45, UP)
        
        red_ray = camera.draw_ray(8, 5, color=RED)
        
        self.add(camera, red_ray)