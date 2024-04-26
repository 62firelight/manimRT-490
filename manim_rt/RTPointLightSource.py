from manim import *

from typing import Sequence
from manim.typing import Point3D


class RTPointLightSource(Sphere):
    def __init__(self,
        center: Point3D = ORIGIN,
        intensity: float = 1,
        color: ManimColor = YELLOW,
        radius: float = 1,
    **kwargs) -> None:
        super().__init__(
            center,
            radius,
            **kwargs
        )
        self.set_color(color)
        
        self.intensity = intensity

    def get_illumination_at(
        self, 
        point: np.ndarray | tuple[float]
    ) -> float:
        distance_to_object = np.linalg.norm(point - self.get_center())
        
        illumination = self.intensity / (distance_to_object * distance_to_object)
        
        return illumination