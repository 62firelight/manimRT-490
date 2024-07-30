from manim import *

from manim_rt.RTPlane import RTPlane
from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.Ray3D import Ray3D

class Eye3DTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=-90 * DEGREES)
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        eye = ImageMobject("Eye.png").rotate(-45 * DEGREES).shift([-4, 0, 1])
        
        light = RTPointLightSource([4, 0, 1])
    
        ray1 = Line3D([4, 0, 1], [0, 0, -3], color=YELLOW)
        ray2 = Ray3D([0, 0, -3], [-1, 0, 1], distance=3.5, color=YELLOW)
        
        miss1 = Line3D([3.5, 0.25, 1], [0, 0.25, -3], color=YELLOW)
        miss2 = Ray3D([0, 0.25, -3], [-1, 0, 1.5], distance=3.5, color=YELLOW)
        
        plane = RTPlane([0, 0, -3], x_scale=5, y_scale=1.5, color=BLUE, opacity=0.75)
        
        self.add(eye, light, ray1, ray2, miss1, miss2, plane)
        
        # self.play(GrowFromCenter(eye))
        # self.play(Create(ray))