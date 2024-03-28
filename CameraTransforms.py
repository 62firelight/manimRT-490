from manim import *
from manim_rt import Camera


class CameraTransforms(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 45 * DEGREES, theta = -85 * DEGREES, gamma = 95 * DEGREES, zoom = 1)
        
        camera = Camera.drawCamera(projection_point_coords=[0.5, 0, 3], focal_length=5)
        
        y_axis_translation_text = Text("Translation along Y axis")
        y_axis_translation_text.to_edge(DOWN)
        
        x_axis_text = Text("Rotation along X axis")
        x_axis_text.to_edge(DOWN)
        y_axis_text = Text("Rotation along Y axis")
        y_axis_text.to_edge(DOWN)
        z_axis_text = Text("Rotation along Z axis")
        z_axis_text.to_edge(DOWN)
        
        self.add(camera)
        self.add_fixed_in_frame_mobjects(y_axis_translation_text)
        
        # Translation along Y axis
        self.play(camera.animate.shift(4 * UP))
        self.play(camera.animate.shift(7 * DOWN))
        self.play(camera.animate.shift(3 * UP))
        
        # Rotation along X axis
        self.play(Transform(y_axis_translation_text, x_axis_text))
        self.play(Rotate(camera, 360 * DEGREES, RIGHT, run_time=3))
        
        # Rotation along Y axis
        self.play(Transform(y_axis_translation_text, y_axis_text))
        self.play(Rotate(camera, 360 * DEGREES, UP, run_time=3))
        
        # Rotation along Z axis
        self.play(Transform(y_axis_translation_text, z_axis_text))
        self.play(Rotate(camera, 360 * DEGREES, OUT, run_time=3))