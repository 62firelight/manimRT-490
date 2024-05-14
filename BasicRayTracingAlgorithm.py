from manim import *

from manim_rt.RTCamera import RTCamera
from manim_rt.RTPlane import RTPlane
from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.RTSphere import RTSphere
from manim_rt.Ray3D import Ray3D

class BasicRayTracingAlgorithm(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=0*DEGREES, zoom=1.5, frame_center=[0, 0, 1.5])

        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        red_sphere_location = [0, 2, 2]
        
        # Camera
        ray_start = [2, -3, 3]
        camera = RTCamera(ray_start, plane_width=3, plane_height=3).rotate(90 * DEGREES, RIGHT).rotate(45 * DEGREES, OUT)
        # ray = Ray3D(ray_start, np.subtract(red_sphere_location, ray_start), color=GREEN)
        ray = camera.draw_ray(2, 2)
        
        # Scene
        plane = RTPlane(x_scale=1.5, y_scale=4)
        transparent_sphere = RTSphere(translation=[0, 0, 1], opacity=0.5)
        red_sphere = RTSphere(translation=red_sphere_location, color=RED)
        light_source = RTPointLightSource([0, -0.5, 3]).scale(0.25)
        
        self.add(axes, labels)
        
        self.add(camera)
        
        self.add(ray)
        
        self.add(plane, transparent_sphere, red_sphere, light_source)