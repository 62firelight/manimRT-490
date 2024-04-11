from manim import *

from manim_rt.Ray3D import Ray3D

class RayTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=25 * DEGREES)
        
        ray = Ray3D(ORIGIN, [0, 1, 0], 3, color=BLUE)
        
        self.add(ray)