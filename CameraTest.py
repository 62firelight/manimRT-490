from manim import * 
from manim_rt import *
from manim_rt.RTCamera import RTCamera
from manim_rt.Ray3D import Ray3D
 

class CameraTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=-95*DEGREES, zoom=8)
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        camera = RTCamera([0, 0, 1])
        
        red_ray = camera.draw_ray(8, 5, color=RED, distance=1.5, thickness=0.01)
        green_pixel = camera.colour_pixel(8, 5, color=GREEN)
        
        self.add(axes, labels, camera, red_ray, green_pixel)