from manim import *

import numpy as np

class Ray3D(Arrow3D):
    def __init__(
        self,
        start: np.ndarray = LEFT,
        direction: np.ndarray = RIGHT,
        distance: float = 1,
        thickness: float = 0.02,
        color: ParsableManimColor = WHITE,
        **kwargs,
    ) -> None:
        # TODO: Normalize the direction
        self.direction = direction
        
        end = start + distance * np.array(self.direction)
        
        super().__init__(
            start=start, end=end, thickness=thickness, color=color, **kwargs
        )
        
        self.distance = distance
        