from manim import *

class ROITitle(ThreeDScene):
    def construct(self):
        title = Text("Ray-Object Intersections")
        
        self.play(FadeIn(title))
        self.wait()
        self.play(FadeOut(title))