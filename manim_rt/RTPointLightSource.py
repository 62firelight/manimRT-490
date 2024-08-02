from manim import *

from typing import Sequence
from manim.typing import Point3D


class RTPointLightSource(Sphere):
    """A sphere that represents a light source within a scene.
    
    Parameters
    ----------
    center
        The location of the light source's centre.
    intensity
        The intensity of the light source.
    color
        The color of the light source. By default, this is set to yellow.
    radius
        The radius of the light source.
    """
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

    """Calculates the illumination of a given point from this light source.
    
    Parameters
    ----------
    point
        The point that is illuminated by a light source.
        
    Returns
    -------
    The illumination value of the point (i.e. how bright this point will be 
    as a result of this light source).
    """
    def get_illumination_at(
        self, 
        point: np.ndarray | tuple[float]
    ) -> float:
        distance_to_object = np.linalg.norm(point - self.get_center())
        
        illumination = self.intensity / (distance_to_object * distance_to_object)
        
        return illumination