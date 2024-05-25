from manim import * 
from manim_rt import *
from manim_rt.RTCamera import RTCamera
from manim_rt.Ray3D import Ray3D
 

class CameraTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=-95*DEGREES, zoom=8)
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        # self.set_camera_orientation(phi = 55 * DEGREES, theta = -90 * DEGREES, gamma = 90 * DEGREES, zoom = 1.25)
        
        camera = RTCamera([0, 0, 1])
        # camera.rotate(-45, UP)
        
        red_ray = camera.draw_ray(8, 5, color=RED, distance=1.5, thickness=0.01)
        green_pixel = camera.colour_pixel(8, 5, color=GREEN)
        
        # square = Square(side_length=1, stroke_opacity=0, fill_opacity=1, fill_color=RED, shade_in_3d=True)
        # square.stretch(1/camera.plane_width, 0)
        # square.stretch(1/camera.plane_height, 1)
        
        # square.shift(camera.c2p(0.5, -0.5))
        
        self.add(axes, labels, camera, red_ray, green_pixel)