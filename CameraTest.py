from manim import * 
from manim_rt import *
from manim_rt.RTCamera import RTCamera
from manim_rt.Ray3D import Ray3D
 

class CameraTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=-45*DEGREES, frame_center=[0, 0, 0.25], zoom=5.5)
        camera = RTCamera([0, 0, 1], focal_length=1)
        red_ray = camera.draw_ray(8, 5, color=RED, distance=1.75, thickness=0.005)
        self.add(camera, red_ray)
        # self.set_camera_orientation(phi=65*DEGREES, theta=-95*DEGREES, zoom=8)
        # axes = ThreeDAxes()
        # labels = axes.get_axis_labels()
        
        # camera = RTCamera([0, 0, 1])
        
        # red_ray = camera.draw_ray(8, 5, color=RED, distance=1.5, thickness=0.01)
        # green_pixel = camera.colour_pixel(8, 5, color=GREEN)
        
        # self.add(camera, red_ray, green_pixel)