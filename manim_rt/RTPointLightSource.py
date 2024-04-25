from manim import *

from typing import Sequence
from manim.typing import Point3D


class RTPointLightSource(Sphere):
    def __init__(self,
        center: Point3D = ORIGIN,
        color: ManimColor = YELLOW,
        radius: float = 1,
    **kwargs) -> None:
        super().__init__(
            center,
            radius,
            **kwargs
        )
        self.set_color(color)