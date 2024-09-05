from manim import *
from manim_rt import *


class ManimRTExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=-135*DEGREES, zoom=1.5) 
        sphere = RTSphere(color=BLUE)
        ray = Ray3D([-5, 0, 0], length=10, color=RED)
        self.begin_ambient_camera_rotation(0)
        self.play(GrowFromCenter(sphere))
        self.play(Create(ray, run_time=2))
        self.wait(2)