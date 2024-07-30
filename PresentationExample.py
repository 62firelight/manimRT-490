from manim import *

from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class PresentationExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=-135*DEGREES, zoom=1.5)
        
        sphere = RTSphere(color=GREEN)
        
        ray = Ray3D([-5, 0, 0], distance=10, color=RED)
        
        self.begin_ambient_camera_rotation(0)
        
        self.add(sphere)
        
        # self.wait(2)
        
        self.play(Create(ray, run_time=2))
        
        self.wait(2)
        
        
        
        