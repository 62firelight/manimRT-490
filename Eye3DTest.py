from manim import *

from manim_rt.Ray3D import Ray3D

class Eye3DTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES)
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        eye = ImageMobject("Eye.png")
        
        ray = Ray3D([5, 0, 0], LEFT, distance=4.1, color=YELLOW)
        
        # self.add(axes, labels, eye, ray)
        
        self.play(GrowFromCenter(eye))
        self.play(Create(ray))