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
        
        red_sphere_location = [-1, 2, 2]
        
        # Camera
        ray_start = [2, -2.5, 3]
        camera = RTCamera(ray_start, image_width=3, image_height=3).rotate(90 * DEGREES, RIGHT).rotate(35 * DEGREES, OUT)
        partial_ray = camera.draw_ray(2, 2, 2)
        ray = camera.draw_ray(2, 2, 7.5)
        # ray1 = camera.draw_ray(1, 1, 7.5)
        # ray2 = camera.draw_ray(2, 1, 7.5)
        # ray3 = camera.draw_ray(3, 1, 7.5)
        # ray4 = camera.draw_ray(1, 2, 7.5)
        # ray5 = camera.draw_ray(3, 2, 7.5)
        # ray6 = camera.draw_ray(1, 3, 7.5)
        # ray7 = camera.draw_ray(2, 3, 7.5)
        # ray8 = camera.draw_ray(3, 3, 7.5)
        
        pixel = camera.colour_pixel(2, 2, RED).rotate(90 * DEGREES, RIGHT).rotate(35 * DEGREES, OUT)
        
        # Scene
        plane = RTPlane(x_scale=1.5, y_scale=4)
        transparent_sphere = RTSphere(translation=[0, 0, 1], opacity=0.5)
        red_sphere = RTSphere(translation=red_sphere_location, color=RED)
        light_source = RTPointLightSource([0, -0.5, 3]).scale(0.25)
        
        # Image
        self.add(axes)
        self.add(labels)
        self.add(camera)
        # self.add(partial_ray)
        self.add(ray)
        self.add(pixel)
        # self.add(plane)
        # self.add(transparent_sphere)
        # self.add(red_sphere)
        # self.add(light_source)
        # self.add(ray1)
        # self.add(ray2)
        # self.add(ray3)
        # self.add(ray4)
        # self.add(ray5)
        # self.add(ray6)
        # self.add(ray7)
        # self.add(ray8)
        
        # Animations
        # self.begin_ambient_camera_rotation(0)
        
        # self.play(GrowFromCenter(camera))
        # self.play(GrowFromCenter(plane))
        # self.play(GrowFromCenter(red_sphere))
        # self.play(GrowFromCenter(transparent_sphere))
        # self.play(GrowFromCenter(light_source))
        # self.play(Create(partial_ray))
        # self.play(FadeOut(partial_ray))
        # self.play(Create(ray))
        # self.play(Create(ray1))
        # self.play(Create(ray2))
        # self.play(Create(ray3))
        # self.play(Create(ray4))
        # self.play(Create(ray5))
        # self.play(Create(ray6))
        # self.play(Create(ray7))
        # self.play(Create(ray8))
        