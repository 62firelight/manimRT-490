from manim import *

from manim_rt.RTCamera import RTCamera
from manim_rt.RTPlane import RTPlane
from manim_rt.RTPointLightSource import RTPointLightSource
from manim_rt.Ray3D import Ray3D

class WhatIsRayTracing(ThreeDScene):
    def construct(self):
        # side-on view
        # self.set_camera_orientation(phi=45 * DEGREES, theta=-90 * DEGREES)
        self.set_camera_orientation(phi=85 * DEGREES, theta=-120 * DEGREES, zoom=1.75)
        
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        
        viewer_location = [-3, 0, 0]
        
        light_source_location = [3, 0, 0]
        
        eye = ImageMobject("Eye.png").stretch(2, 1).shift(viewer_location)
        
        light = RTPointLightSource(light_source_location, color=ORANGE)
        
        camera = RTCamera(viewer_location, 3, 3).shift([0, 0, 0.45]).rotate(-90 * DEGREES, UP)
        
        ray = camera.draw_ray(2, 2, 5.5, color=YELLOW)
        pixel = camera.colour_pixel(2, 2, color=ORANGE).rotate(-90 * DEGREES, UP)
        
        photon = Ray3D(light_source_location, -ray.direction, length=5.15, color=YELLOW)
        longer_photon = Ray3D(light_source_location, -ray.direction, length=6.1, color=YELLOW)
        
        plane = RTPlane([0, 0, -1], x_scale=5, y_scale=1.5, color=BLUE, opacity=0.75)
        
        self.begin_ambient_camera_rotation(0)
        
        # self.add(axes)
        # self.add(labels)
        # self.add(light)
        # self.add(eye)
        # self.add(photon)
        # self.add(camera)
        # self.add(longer_photon)
        # self.add(ray)
        # self.add(pixel)
        # self.add(plane)
        
        self.play(GrowFromCenter(eye))
        self.play(GrowFromCenter(light))
        self.play(Create(photon, run_time=1.5))
        self.play(FadeOut(eye, photon))
        self.play(GrowFromCenter(camera))
        self.play(Create(longer_photon, run_time=1.5))
        self.play(FadeOut(longer_photon))
        self.play(Create(ray, run_time=1.5))
        self.play(FadeIn(pixel))