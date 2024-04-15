from manim import * 
from manim_rt import *
from manim_rt.RTCamera import RTCamera
from manim_rt.Ray3D import Ray3D
 

class CameraTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=-20 * DEGREES)
        
        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())
        
        camera = RTCamera()
        
        ray = Ray3D([0, 0, 1], [1, 0, 0], 3)
        
        self.add(camera, ray)