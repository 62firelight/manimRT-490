from manim import *

# Source: aman00__ and uwezi in the Manim discord
# This code was modified so that it was closer to the center of the lines
class Arc3D(ArcBetweenPoints):
    def __init__(
        self, 
        line1, 
        line2, 
        color=WHITE
    ):        
        line1_center = line1.get_center()
        line2_center = line2.get_center()
        
        super().__init__(line2_center, line1_center, radius=1, color=color)