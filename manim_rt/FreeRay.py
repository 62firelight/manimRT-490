from manim import *

from manim_rt.Ray import Ray


class FreeRay(Ray):
    def __init__(self, start_point, direction, distance=2, color=BLUE):
        end_point = start_point + distance * np.array(direction)
        
        super().__init__(start_point, end_point, distance, color)