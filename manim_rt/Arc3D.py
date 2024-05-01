from manim import *

# Source: aman00__ and uwezi in the Manim discord
class Arc3D(ArcBetweenPoints):
    def __init__(self, line1, line2, color=WHITE):    
        dot1 = Dot3D().move_to((line1.get_end() - line1.get_start()) / 2)          
        dot2 = Dot3D().move_to((line2.get_end() - line2.get_start()) / 2)
        
        super().__init__(dot1.get_center(), dot2.get_center(), radius=1, color=color)